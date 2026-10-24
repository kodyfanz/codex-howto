"""Render the small, intentionally supported Mermaid subset used by the guide.

The curriculum currently uses flowcharts with labelled rectangular nodes and
directed arrows. This renderer keeps builds dependency-free and offline while
producing real SVG diagrams for both the website and EPUB. The original
Mermaid source remains available as an accessible disclosure block.
"""

from __future__ import annotations

import html
import math
import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    key: str
    label: str


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str = ""


NODE_RE = re.compile(r"(?P<key>[A-Za-z][\w-]*)\s*\[(?P<label>[^\]]+)\]")
EDGE_RE = re.compile(
    r"(?P<source>[A-Za-z][\w-]*)(?:\[[^\]]+\])?\s*-->(?:\|(?P<label>[^|]+)\|)?\s*(?P<target>[A-Za-z][\w-]*)(?:\[[^\]]+\])?"
)


def parse_flowchart(source: str) -> tuple[str, list[Node], list[Edge]]:
    lines = [line.strip() for line in source.splitlines() if line.strip() and not line.lstrip().startswith("%%")]
    if not lines or not re.match(r"^(flowchart|graph)\s+(LR|TD|TB|RL|BT)$", lines[0]):
        raise ValueError("only flowchart/graph LR, RL, TD, TB, or BT is supported")
    direction = lines[0].split()[-1]
    nodes: dict[str, Node] = {}
    edges: list[Edge] = []
    for line in lines[1:]:
        for match in NODE_RE.finditer(line):
            nodes.setdefault(match.group("key"), Node(match.group("key"), match.group("label").strip()))
        for match in EDGE_RE.finditer(line):
            source_key = match.group("source")
            target_key = match.group("target")
            nodes.setdefault(source_key, Node(source_key, source_key))
            nodes.setdefault(target_key, Node(target_key, target_key))
            edges.append(Edge(source_key, target_key, (match.group("label") or "").strip()))
    if not nodes:
        raise ValueError("flowchart contains no nodes")
    return direction, list(nodes.values()), edges


def _rank_nodes(nodes: list[Node], edges: list[Edge]) -> dict[str, int]:
    rank = {node.key: 0 for node in nodes}
    # A bounded relaxation handles chains while remaining stable for cycles.
    for _ in range(len(nodes)):
        changed = False
        for edge in edges:
            value = rank[edge.source] + 1
            if value > rank[edge.target]:
                rank[edge.target] = value
                changed = True
        if not changed:
            break
    if any(rank[edge.source] >= rank[edge.target] for edge in edges):
        rank = {node.key: index for index, node in enumerate(nodes)}
    return rank


def _wrap_label(label: str, limit: int = 25) -> list[str]:
    words = label.split()
    lines: list[str] = []
    current = ""
    for word in words:
        if current and len(current) + len(word) + 1 > limit:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}".strip()
    if current:
        lines.append(current)
    return lines or [""]


def render_svg(source: str, title: str = "Mermaid flowchart") -> str:
    """Return a standalone accessible SVG for a supported flowchart."""
    direction, nodes, edges = parse_flowchart(source)
    rank = _rank_nodes(nodes, edges)
    groups: dict[int, list[Node]] = {}
    for node in nodes:
        groups.setdefault(rank[node.key], []).append(node)
    node_width = 190
    node_gap = 55
    axis_gap = 95
    positions: dict[str, tuple[float, float, float, float]] = {}
    horizontal = direction in {"LR", "RL"}
    max_group = max(len(group) for group in groups.values())
    axis_count = max(rank.values()) + 1
    width = max(460, axis_count * (node_width + axis_gap) + 80) if horizontal else max(460, max_group * (node_width + node_gap) + 80)
    height = max(190, max_group * 105) if horizontal else max(190, axis_count * 145 + 50)
    for axis, group in groups.items():
        for offset, node in enumerate(group):
            lines = _wrap_label(node.label)
            node_height = max(48, 24 + len(lines) * 18)
            if horizontal:
                x = 40 + axis * (node_width + axis_gap)
                y = (height - node_height) / 2 + (offset - (len(group) - 1) / 2) * (node_height + node_gap)
            else:
                x = (width - node_width) / 2 + (offset - (len(group) - 1) / 2) * (node_width + node_gap)
                y = 30 + axis * 145
            positions[node.key] = (x, y, node_width, node_height)

    defs = '''<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#075c4b"/></marker></defs>'''
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {math.ceil(width)} {math.ceil(height)}" role="img" aria-labelledby="title desc">',
        defs,
        f'<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape("Diagram generated from Mermaid source")}</desc>',
        '<rect width="100%" height="100%" fill="#fffdf7" rx="12"/>',
    ]
    for edge in edges:
        sx, sy, sw, sh = positions[edge.source]
        tx, ty, tw, th = positions[edge.target]
        if horizontal:
            start_x = sx + sw if tx >= sx else sx
            end_x = tx if tx >= sx else tx + tw
            start_y = sy + sh / 2
            end_y = ty + th / 2
        else:
            start_x = sx + sw / 2
            end_x = tx + tw / 2
            start_y = sy + sh if ty >= sy else sy
            end_y = ty if ty >= sy else ty + th
        parts.append(f'<path d="M {start_x:.1f} {start_y:.1f} L {end_x:.1f} {end_y:.1f}" fill="none" stroke="#075c4b" stroke-width="2" marker-end="url(#arrow)"/>')
        if edge.label:
            parts.append(f'<text x="{(start_x + end_x) / 2:.1f}" y="{(start_y + end_y) / 2 - 7:.1f}" text-anchor="middle" fill="#34584d" font-size="13">{html.escape(edge.label)}</text>')
    for node in nodes:
        x, y, width_node, height_node = positions[node.key]
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{width_node:.1f}" height="{height_node:.1f}" rx="10" fill="#d8ebe4" stroke="#075c4b" stroke-width="2"/>')
        lines = _wrap_label(node.label)
        start_y = y + height_node / 2 - (len(lines) - 1) * 8
        for index, line in enumerate(lines):
            parts.append(f'<text x="{x + width_node / 2:.1f}" y="{start_y + index * 18:.1f}" text-anchor="middle" dominant-baseline="middle" fill="#16221d" font-family="system-ui, sans-serif" font-size="14">{html.escape(line)}</text>')
    parts.append("</svg>")
    return "".join(parts)
