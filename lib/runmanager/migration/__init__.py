"""The migration path (plan-run-manager.md 04). `scan` finds the new work and cuts the batches when a
migration run starts (spec-run-manager.md 07.1; 07.2). `record`, `findings`, and `undo` run each batch's
cycle, with `cycle` holding their shared paths and steps (04 item 22; 09.1; CONTRACT.md 5.3)."""
