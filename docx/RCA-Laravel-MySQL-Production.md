# RCA Draft: Laravel production — MySQL 2006 (intermittent API 500s)

## Incident summary

Production API traffic on Laravel 9 (Nginx + PHP-FPM on Ubuntu, MySQL on AWS RDS, Redis + Horizon, zero-downtime CI/CD deploys) began showing **intermittent HTTP 500** responses after a **recent deployment**. Failures are **not consistent** from request to request. Reported application error: `SQLSTATE[HY000]: General error: 2006 MySQL server has gone away`. **Existing API endpoints** are affected; **new endpoint(s) introduced in the same deployment** are reported as **working**. **Queue processing (Horizon)** is reported as **okay** for the same period. The issue **still occurs sometimes**. Application CPU and memory were reported as **normal**; **database connection counts** were observed to **spike under peak load**. **PDO persistent connections** are enabled in `config/database.php`, and queue workers are **long-lived** processes.

## Impact

- **Who / what:** API consumers hitting **existing** endpoints; intermittent **5xx** responses.
- **Magnitude:** approximately **2–15%** of requests affected — **approximate, measurement method pending** (define route scope, time window, and source: dashboards, logs, or APM).
- **Duration / status:** First team-visible detection at **approximately 13:00 Asia/Kolkata (IST, UTC+5:30)** — **07:30 UTC on the same calendar day once the date is confirmed**; **ongoing intermittent** failures at time of reporting.
- **SLA / contractual impact:** `pending` (include only if verified).

## Timeline

*Time basis: local detection stated in IST; final published timeline should use one consistent basis (**UTC recommended**) once the calendar date is fixed.*

- `**pending` (calendar date):** Confirm the **date** for first detection at **~13:00 IST** (e.g. align to **Sentry** / ticketing).
- ~~**13:00 IST (~~07:30 UTC on confirmed date):** **Detected** via **application logs**, **user reports**, and a **Sentry** alert.
- `**pending` (exact timestamp UTC):** **Recent deployment** that preceded or coincided with the issue — record **deploy identifier** (pipeline run, release tag, or commit) when available.
- **After deploy:** A **new MySQL table** was introduced and **migrated**; migration is reported **successful** and the **new module is reported working**. **Intermittent 500s on existing endpoints** were reported **before and after** this work. **Whether this schema change was intended to address the 2006 errors** is `**pending` confirmation** (if it was opportunistic or unrelated, state that explicitly once known).
- `**pending`:** Evidence review confirming whether **Horizon / `failed_jobs`** show the **same** `2006` error in the **same time window** as HTTP failures (strengthens or weakens an HTTP-only failure pattern).

## Root cause

`**pending` — not yet verified** against primary evidence (for example: RDS / MySQL metrics and configuration at failure time, a **single** failed request traced end-to-end from edge to query, and comparison of **failing vs non-failing** routes).

**Candidate mechanisms (not validated — conditional language only):**

- Intermittent **client–database connection loss** consistent with **2006**, in an environment where **persistent PDO** and **idle** or **long-held** connections may interact with **server-side or network idle limits** — **to be validated**, not asserted.
- **Differential behavior** between **existing** and **new** routes could reflect **traffic mix**, **middleware**, **caching**, **read/write** usage, or **code path** differences — **not concluded** from asymmetry alone.

**Evidence required to close (checklist):**

- **Sentry** + **Laravel** log correlation for at least one failure: **timestamp (UTC), route, request id**, and full stack context (no secrets or unnecessary PII in the RCA body).
- **RDS** snapshot for the incident window: **connection count**, relevant **parameter group** settings (e.g. `**wait_timeout`**, `**max_connections**`), and any **instance events** aligned to errors.
- **Deploy record**: **UTC time**, **change list** (config, migrations, routes), and ordering vs **first error**.
- **Queue audit**: search **worker / Horizon** logs and `**failed_jobs`** for `**2006` / server has gone away** over the **same window** as HTTP errors.
- **Load vs. route** view: whether **new** routes receive materially **less traffic** than **existing** ones during incidents (avoids over-interpreting “new works, old fails”).

## Solution

`**pending`.** A **verified corrective change** that **eliminates** intermittent **500s** / **2006** on **existing** endpoints is **not yet confirmed** in this record. The **new table** and **migration** are **factual** outcomes; their **role** in resolving this incident is `**pending`** (see Timeline).

## Action items

- [pending] **Owner TBD / Due TBD — P1:** Trace **one** production failure end-to-end (**Sentry** ↔ **Laravel** ↔ **RDS** time alignment); capture **route name** and **UTC timestamp**.
- [pending] **Owner TBD / Due TBD — P1:** Document **deploy** (**UTC**, **ID/tag**) and **diff** vs prior release (config, DB, routes).
- [pending] **Owner TBD / Due TBD — P1:** Export or screenshot **RDS** metrics + **parameter group** for the spike window (**connection count**, timeouts); store in secure incident notes, reference link only in RCA.
- [pending] **Owner TBD / Due TBD — P2:** Define how **2–15%** was computed; replace **approximate** with **measured** error rate or retain **approximate** with **method documented**.
- [pending] **Owner TBD / Due TBD — P2:** **Horizon / `failed_jobs` / worker logs** — confirm or rule out **2006** in workers for the same period as HTTP incidents.
- [pending] **Owner TBD / Due TBD — P2:** Review `**config/database.php`** **persistent** setting and **worker lifetime / recycling** policy vs **MySQL / RDS** idle behavior; decision recorded with **evidence**.
- [pending] **Owner TBD / Due TBD — P3:** **Monitoring**: error rate **by route**, **RDS connections**, alerts; tune thresholds after root cause is known.

## Mitigation plan

`**pending`:** Prevention, earlier detection, and faster recovery to be defined **after** root cause is verified — may include connection handling, **RDS** tuning or **proxy/pooling**, timeouts, **deploy + worker** practices, and **load testing** that reproduces production connection patterns. No mitigation should be presented as **complete** in this document until **evidence** shows reduced or eliminated recurrence for **existing** endpoints.

## Evidence pointers (secure references — fill when available)


| Artifact                                 | Reference (no secrets)              |
| ---------------------------------------- | ----------------------------------- |
| Sentry issue(s)                          | `pending`                           |
| Laravel logs (path / viewer / retention) | `pending`                           |
| Deploy pipeline run / tag                | `pending`                           |
| RDS dashboard / Performance Insights     | `pending`                           |
| Ticket / incident ID                     | `pending` (none reported at intake) |


