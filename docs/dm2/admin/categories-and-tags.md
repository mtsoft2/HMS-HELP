# Categories & Tags

Three free-text fields are attached to every document — **Category**,
**Tags**, **Keywords**. They look similar but behave differently.

## Category

* **One per document** — radio-button choice.
* Picked from a **controlled list** the admin maintains.
* Shown as a coloured badge on every tile.
* Drives the Category filter dropdown above the gallery.
* The right value to use for a strong taxonomy you can later filter
  and report on.

### Typical categories

* X-ray
* Photo
* Consent form
* Lab result
* Referral letter
* Prescription
* Invoice / receipt
* ID document
* Insurance card
* Treatment plan
* Discharge summary
* Other

The list is configurable per clinic — keep it short (12 – 20 items
maximum). Long lists confuse users and dilute the value of filtering.

## Tags

* **Many per document** — comma-separated free text.
* Not validated — users type whatever they want.
* Searchable from the gallery search bar.
* Good for **ad-hoc grouping** that doesn't deserve a category: *pre-op*,
  *post-op*, *insurance-claim*, *re-do*, *referred-out*.

### Tip — agree a tag vocabulary

Free-form tags drift fast. Publish a short tag list (10 – 20 tags) and
ask the team to stick to it. Otherwise *preop*, *pre-op*, *Pre-Op*, and
*pre op* all end up as four different tags.

## Keywords

* Free text, single field.
* Same as tags from a search point of view (the gallery search box
  matches all three).
* Use **Keywords** for searchable content that doesn't fit a short tag
  — e.g. the patient's reported symptom in their own words ("upper
  right molar pain since Monday"), or OCR'd content from a scanned
  document.

## Where the three fields show up

| UI | Category | Tags | Keywords |
|---|---|---|---|
| Tile badge | Yes (coloured) | No | No |
| Filter dropdown above gallery | Yes | No | No |
| Search box | Yes | Yes | Yes |
| Edit dialog | Picker | Comma-separated input | Comma-separated input |
| Import dialog (bulk) | Single value applied to all | Same | Same |
