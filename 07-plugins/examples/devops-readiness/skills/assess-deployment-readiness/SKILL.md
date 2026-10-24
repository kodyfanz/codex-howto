---
name: assess-deployment-readiness
description: Assess whether a deployment plan has sufficient evidence, rollback steps, ownership, and monitoring. Use for pre-deployment readiness review. Do not deploy, approve, or mutate infrastructure.
---

# Assess Deployment Readiness

Review the proposed version, target environment, dependencies, validation
evidence, rollout sequence, observability, ownership, and rollback trigger.
Separate confirmed facts from missing evidence.

If the user supplies a JSON plan matching the bundled example, run:

```bash
python3 "$PLUGIN_ROOT/scripts/check_deployment_plan.py" path/to/plan.json
```

The validator checks structure only; it does not prove that a deployment is
safe. Inspect referenced evidence and repository-specific runbooks before
drawing a conclusion.

Return:

1. readiness status: ready for human review, conditionally ready, or not ready;
2. confirmed evidence;
3. blockers and missing evidence;
4. rollback and monitoring gaps;
5. the next safe verification step.

Do not execute deployment, rollback, infrastructure, or external notification
commands. Those actions require a separately authorized workflow and the
environment's normal approvals.
