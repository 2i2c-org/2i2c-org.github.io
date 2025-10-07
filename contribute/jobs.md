# Job postings

## Add a job post

We have some custom Hugo templates created for posting new jobs and a summary of open jobs.

- The `content/jobs/` folder contains all content related to job postings and an overview of working at 2i2c.
- The `/jobs/_index.md` file is a "landing page" for our jobs (what is at 2i2c.org/jobs).
  - It contains a custom Hugo shortcode defined at `layouts/shortcodes/open_jobs.html` that will list all jobs in the `jobs/` folder that have `open: true` in the page metadata.
- Every other page in `/jobs/` is a job posting. The YAML metadata at the top contains several important pieces of information for the job, and is used to populate job posting cards.
  - Use previous job postings as a reference for the information that should be used.
  - To mark a job as "open", make sure to put `open: true` in the posting metadata.
  - There's also a special shortcode to display relevant job metadata for a posting. This is at `layouts/shortcodes/job_details.html`.
