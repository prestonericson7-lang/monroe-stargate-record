# The Monroe files

**What the CIA's declassified STARGATE records say about Robert Monroe, Hemi-Sync, the Gateway Process and the U.S. Army's remote-viewing program, read document by document, and the sealed tests that would settle what those records never did.**

By Preston Ericson, working with Claude (Anthropic's AI) as research partner. Preston chose the question and the frame, pulled the files the reading room serves only as downloads, and decides what is published; Claude read the documents with him, drafted these pages and wrote the one script. Every document is named by its CIA number so a reader can open the same pages and check every line. Nothing here is cited from a summary of a document.

First release: 18 November 2026. The reading was done in one day, in three passes. Each page ends with a list of what was read whole, what was read in part, and what was not read; that last list is the next work.

## If you have ten minutes

1. **The Army and the Monroe Institute, 1978 to 1984.** A field office of Army intelligence proposed in August 1978 to have Robert Monroe train three soldiers to leave their bodies, so that they could "mimic Soviet collectors". Sixty days later the Pentagon's intelligence staff rejected the plan as hypnosis and human experimentation and wrote that "no one in either agency believes that time or money should be spent" on it. It went ahead anyway. In January 1984 the Secretary of the Army was briefed on it for thirty minutes and said "good". (`01`, documents b, c and g.)
2. **The money, every figure in the record.** $2,000 for the 1978 pilot; $24,400 for one-on-one training in 1983, paid from a fund chosen because it "precludes the unauthorized disclosure"; $850 a head for a screening course; $60,000 for fiscal 1984; a plan growing to $700,000 a year. (`02`, S5.)
3. **Congress cut the funding on 1 October 1982. The program continued under a new name, CENTER LANE, on money the command found "out of hide".** That is the Army's own chronology of itself. (`02`, S3.)
4. **The Army's lawyers and doctors called it "human use" three times between 1979 and 1981.** Consent forms appear in the record in 1984. (`02`, S4.)
5. **What the Army believed, and its own test.** The 1983 "Analysis and Assessment of Gateway Process", twenty-nine pages, contains no measurement. The one test it reports is people trying, out of body, to read ten computer-generated numbers in a laboratory across the country: "none have ever succeeded in getting all ten correct". That is the Army's own criterion of success, written by its own analyst. (`01`, document e.)
6. **The first operational use of Monroe's method was the hunt for William Buckley**, the CIA's Beirut station chief, kidnapped on 16 March 1984. On 21 March the viewer, in a Hemi-Sync session with a skin-voltage meter read aloud as a truth gauge, described a city on a river with a domed cathedral and captors from southern Europe. Buckley was held in Lebanon. The one session in the file that can be checked against a map (2 April 1984) matches it three bearings for three, and the viewer had been shown imagery of the suspected site before the session, so the match cannot be told from memory. (`02`, S1; `03`, 2a; `tools/bearings.py`.)
7. **The program's successor at the Defense Intelligence Agency scored itself in 1988 and 1989:** information "of value" about half the time by its customers' word, "high" rarely (3 to 27 percent of evaluated sessions, per viewer), and about the future "simply not marketable". Monroe's hemisphere synchronization was still inside its training protocol in 1989. (`03`, 2b.)
8. **The Institute wrote, in a bulletin the Army kept,** that its work had "not been designed or performed with the intent of offering documentation to the scientific community". Its "4,823 experiments" never became a paper that could be found. (`02`, S10.)
9. **Mind control and ESP meet in one 1961 memo:** MKULTRA Subproject 136 funded "an Experimental Analysis of Extrasensory Perception" with "special attention ... to dissociative states", which "can be induced and controlled to some extent with hypnosis and drugs". (`02`, S9.)
10. **What the record does not contain:** any document showing an ability that worked and was hidden. The famous missing page 25 of the Gateway analysis, absent from the CIA's copy, is in the Institute's own copy, and it is philosophy. (`02`, S11; `documents/`.)
11. **The laboratory record since:** the out-of-body sensation is produced on demand by electrically stimulating one region of the brain; hidden targets in the largest hospital studies went unseen; the effect of intention on random number generators is tiny and could be produced by publication bias alone; whether binaural beats entrain brain rhythms is still unsettled after fourteen studies. (`01`, section 3.)

**The conclusion of the whole file:** in forty years nobody ran a sealed test of Monroe's method with a record anyone could score. The believers never measured, and the evaluators measured only paperwork. The tests in `04_SEALED_TESTS.md` are cheap, exact, and written so that anyone can run them.

## How this repository is laid out

| File | What it is |
|---|---|
| `01_THE_RECORD.md` | Who Monroe was; the government's record from 1972 to 1995, document by document; the laboratory record; the plain reading. |
| `02_THE_SEAMS.md` | The second pass, run as if the record hid something: thirteen seams, ten gaps, the verdict inside the frame and outside it, and the FOIA requests anyone can file. |
| `03_THE_REST_OF_THE_RECORD.md` | The third pass: the Buckley case whole, with the map check; the DIA's own numbers; the 1978 intent; a 1992 verdict from inside; what it all means. |
| `04_SEALED_TESTS.md` | Five test protocols with a sealed hardware monitor, a practitioner's ladder taken from the DIA's own training classes, and the safety rules the record itself teaches. |
| `documents/INDEX.md` | Every document cited, with its CIA number, date, pages, link, and how much of it was read. |
| `documents/` | Copies of the documents the reading room serves only as downloads or in broken form: the Buckley session PDF, the Gateway analysis text and its page 25, and the DIA reports. |
| `tools/bearings.py` | The map check for the one checkable session. Run `python3 tools/bearings.py`. |

Read them in order; each page assumes the one before it.

## How to check any line

- A document page is `https://www.cia.gov/readingroom/document/` followed by the document number in lower case, for example `https://www.cia.gov/readingroom/document/cia-rdp96-00788r001900550001-2`. The scanned PDF is `https://www.cia.gov/readingroom/docs/` followed by the number in upper case and `.pdf`.
- The reading room's search box finds almost nothing by topic. Search by the names: GONDOLA WISH, GRILL FLAME, CENTER LANE, SUN STREAK, STARGATE, "Monroe Institute", Hemi-Sync, and the people's names.
- The map check: `python3 tools/bearings.py` prints the three distances and bearings; the coordinates and their source are at the top of the script.
- The reading room's own OCR of a scan is often broken. The scanned PDF is the authority; where the OCR of a table was broken, only the clearly legible figures are quoted, and the page says so.

## The method

- **Names, not topics.** The files were found by project name and person, not by subject, because the reading room indexes titles and the titles are code names.
- **Read whole, or say how much.** Every document is marked "read whole" or "read in part" with the part named. A document found by search but not opened is listed as such, and nothing is claimed from it.
- **Nothing from summaries.** No claim rests on a search engine's or a secondary source's summary of a document. Where a secondary source is used (two 2020 FOIA letters, a biography page), it is named as secondary.
- **Two readings, kept apart.** A working frame (treat the record as if it hid something, and look for the seams) and a plain reading (what the documents say on their face). Both are on the page; the reader does not have to take the author's.
- **Every number with its source**, and every gap named with its size.
- **Where it ends: a measurement.** The record cannot settle whether anything worked, because nobody sealed a test. The protocols in `04` are the honest next step, and they are written to be run by anyone.

## Glossary for new eyes

- **STARGATE**: the CIA reading room's name for its collection of declassified remote-viewing program files, released from 2000 on. The programs inside it changed names over the years: GONDOLA WISH (the Army's 1977-78 threat study and pilot), GRILL FLAME (from 1978), CENTER LANE (the Army, 1983-84), SUN STREAK (the DIA, from 1985) and STAR GATE (the last name, to 1995). The documents, not this list, are the authority on the dates.
- **Remote viewing (RV)**: describing a distant or hidden target by mental means, in a protocol with a "viewer" who reports and a "monitor" who asks the questions. **CRV** (coordinate remote viewing) and **ERV** (extended remote viewing) are two of the program's protocols; ERV is the one that grew out of Monroe's method.
- **Hemi-Sync**: Robert Monroe's trademarked audio method. Two slightly different tones, one in each ear, make a **binaural beat** inside the brain at their difference frequency; the claim is a **frequency-following response (FFR)** that entrains brain rhythms and synchronizes the two hemispheres.
- **Focus 10, 12, 15, 21**: the Monroe Institute's names for stages of its training. Focus 10 is "mind awake, body asleep"; the Army's analyst describes Focus 15 as the state for reading the past and Focus 21 for the future.
- **Gateway**: the Institute's residential course. The "Gateway Process" analysis is the 1983 Army paper about it.
- **OOBE, out-of-body experience**: perceiving from outside one's own body, Monroe's own starting point in 1958.
- **AOL**: "analytic overlay", the program's word for memory and reasoning leaking into what a viewer reports.
- **INSCOM**: the U.S. Army Intelligence and Security Command, which ran the Army's program. **DIA**: the Defense Intelligence Agency, which took it over in 1985. **ACSI**: the Army's Assistant Chief of Staff for Intelligence.
- **ICF, NFIP, "out of hide"**: money words from the memos. ICF is the intelligence contingency fund the memos name; NFIP is the national foreign intelligence program budget that Congress controls; "out of hide" means paid from a command's own budget with no line of its own.
- **CREST, "released in part", RIPPUB**: the reading room's database and its release markings. "Released in part" means some passages are blacked out; the codes SG1A, SG1J and SGFOIA3 mark what kind of passage was withheld.
- **Sealed test, commit-reveal, hash chain**: the tools of `04`. A hash is a fingerprint of data that cannot be forged backward. Committing a hash before a session and opening the data after it means nobody, the experimenter included, can change the target or the report in between. A hash chain links every record to the one before it, so nothing can be inserted or removed later.

## What this is not

- It is not a claim that remote viewing or out-of-body travel works, and not a claim that it does not. The record cannot say, and this repository says so.
- It is not medical or psychological advice. The practices in the record alter states of mind; the Army's own analyst warned of "dislocating" a person's reality. `04` carries the safety rules the record itself teaches. Anyone with a history of dissociation or trauma should talk to a clinician before practising, and grounding comes before depth.
- It is not finished. The lists of unread documents at the end of each page are the next work, and corrections are kept beside the lines they correct, never written over them.

## License and use

The writing in this repository is released under the Creative Commons Attribution 4.0 license (CC BY 4.0): use it for anything, with credit to Preston Ericson and a link here. The documents in `documents/` are works of the United States government and are in the public domain; the page-25 text comes from the Monroe Institute's copy of the same government document. Corrections and further documents are welcome as issues or pull requests; cite the CIA number.
