# Storage & Deduplication

## Where files live

DM2 stores files in **one of three** places, chosen by the system
configuration:

| Mode | When to pick it | Trade-off |
|---|---|---|
| **OS** | Default. Files are written to the server's upload folder (typically `wwwroot/upload/`). | Fast, simple, easy to back up. |
| **DB** | Files are stored as blobs inside the HMS database. | Single backup covers data + files; database grows fast. |
| **Remote** | Files are streamed to an HMS imaging server (separate machine). | Best for multi-clinic groups sharing one imaging store. |

The choice is set in the system's imaging configuration — typically by
the IT team during install. End users see no difference.

## Upload-folder path

When the storage mode is **OS**, the default location is
`<wwwroot>/upload/`. The admin can redirect it to an absolute path —
useful for pointing at a NAS, shared volume, or large local drive.

Make sure the path is:

* On a **large** disk — imaging fills space fast.
* **Backed up** — files live here, not in the database.
* Reachable by **every** application server in a load-balanced setup.

## File size limits

* Per-file maximum is controlled by the application's request-size
  limit (default 100 MB).
* Per-user upload limit can be set on the user record.
* Browsers also impose their own request size — if a user can't
  upload a large video, try the alternate browser before increasing
  server limits.

## Deduplication

DM2 hashes every uploaded file (SHA-256 of the binary content). On
upload:

1. The hash is computed in the browser before the file is sent.
2. The server checks whether that hash already exists for **this
   patient**.
3. If yes:
   * **Skip duplicate uploads (by content hash)** ON → upload is
     silently skipped; the existing tile is highlighted.
   * **Skip duplicate uploads** OFF → upload proceeds; a small
     duplicate badge appears on the new tile.

The hash check is **per patient**, not global — the same image
attached to two different patients is allowed (they may genuinely
need a copy each).

## Soft delete & retention

Deleted documents move to a recycle bin and stay there until:

* A user with **Hard-delete** permission removes them permanently, or
* A retention sweep runs (configurable) and removes items older than
  the retention window.

The retention sweep is off by default — clinics opt-in once they have
agreed a retention policy with their compliance team.

## Audit

Every upload, edit, delete, restore, and download is logged with
user, timestamp, and document ID. The log is queryable from the
system audit module (outside DM2).
