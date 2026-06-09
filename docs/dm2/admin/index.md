# Administration

DM2 has two areas the administrator owns:

* [Categories & Tags](categories-and-tags.md) — the dropdown the user
  picks from when filing a document.
* [Storage & Deduplication](storage-and-deduplication.md) — where files
  are kept, how big they can be, how duplicates are handled.

## Per-user permissions

Set on the HMS user record (system administration, outside DM2):

| Permission | Effect when off |
|---|---|
| Upload | Hides Add / Import / Capture buttons. |
| Edit metadata | Hides the Edit dialog; titles / tags / categories become read-only. |
| Edit document content | Hides the document editor; Word docs open read-only. |
| Soft-delete | Hides the Delete action; documents cannot be sent to the recycle bin. |
| Hard-delete | Hides Permanently delete; soft-deleted items can only be restored. |
| Restore | Hides Restore on soft-deleted items. |
| Annotate | Hides annotation + measurement tools. |
| Compare | Hides Add to compare. |

These permissions compose with the embedding context's read-only flag
— if either says read-only, the user gets read-only.
