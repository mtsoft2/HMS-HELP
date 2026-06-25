# Settings

You set the NPHIES module up once, then rarely touch it. The settings open in a
small window with a few tabs.

## Provider

Your facility's details and the codes NPHIES expects.

- **Identity** — your facility name, license, and type.
- **Specialty** — your main specialty for outpatient doctor visits. Pick one and
  it fills the code and name for you. Leave it empty and the system uses the
  specialty recorded on each visit instead.
- **Vision** — for eye and optical centers only: the vision product code NPHIES
  recognises. Enter the System, Code, and Display your coordinator gives you, and
  it takes effect on the next run. Leave it empty if you don't do optical work.

## Environment

Decides whether your requests go to the NPHIES **practice** system or the
**real** one.

- **Test Mode** — on means practice (safe, nothing affects real patients); off
  means live.
- **Optical Center** — turn on only if your facility is an eye/optical centre;
  it shows the optical items on the testing screen.
- **Show "Send to Sandbox"** — adds an extra button on the Claims and
  Pre-authorization screens so you can try one on the practice system first, even
  while you're working live.

## Endpoints

The two web addresses your requests are sent to — one for the NPHIES practice
system and one for the real system. They're kept separately so you can switch
between them on the Environment tab without retyping. **NPHIES provides these;
you usually don't need to change them.**

## Bridge

Only needed when your system sits **outside Saudi Arabia**. The bridge is a small
helper inside the country that receives your requests and passes them on to
NPHIES.

- **Use Bridge** — turn on if your system is outside Saudi Arabia.
- **Bridge Proxy URL** — the address of the helper. Your IT team or NPHIES
  coordinator provides it.
- **Bridge Password** — proves you're allowed to use the helper. It must match
  the one set on the bridge.
- **Test Connection** — checks the bridge is reachable **and** tells you whether
  the password is accepted, so you know straight away if either is wrong.

!!! warning "Keep the bridge password private"
    The bridge password is a shared secret. Don't email it, screenshot it, or
    write it where others can see it. If it leaks, have it changed on the bridge.

!!! tip
    After filling Settings in, run a few cases in the [Testing area](screens/testing.md)
    on practice mode to confirm everything is wired up before going live.

**See also:** [Getting started →](getting-started.md) · [The workflow →](workflow/index.md)
