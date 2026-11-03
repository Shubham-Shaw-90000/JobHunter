# JOBHUNTER
## Master Product Description & Implementation Blueprint

**Document Type:** Primary Product Requirements & Implementation Blueprint  
**Version:** 1.0  
**Status:** Approved for detailed planning  
**Project Category:** Personal AI-powered Career Management Platform  
**Development Approach:** AI-assisted, modular, incremental development  
**Primary User:** Single-user personal application  
**Operating Budget:** Zero-cost infrastructure and AI usage initially  
**Primary Objective:** Discover, evaluate, organise and manage employment opportunities across India and international remote markets.

---

# 1. PRODUCT OVERVIEW

## 1.1 Product Vision

JobHunter is a personalised, AI-powered career management platform designed to manage the complete job-search lifecycle.

It will continuously discover employment opportunities from company career portals, job boards and supported external sources. It will evaluate each opportunity against the user's academic background, skills, experience, projects, preferences and evolving career profile.

Qualified opportunities will be presented in a centralised review queue, with concise job information, suitability assessments and direct links to the original job postings.

JobHunter will additionally manage application progress, monitor application-related emails, identify suspicious job postings and correspondence, and generate customised resumes based on individual job descriptions.

The system will continuously maintain a structured record of the user's professional development, ensuring that new skills, projects and achievements can improve future job recommendations and resume generation.

**Core philosophy:**

One platform to discover opportunities, understand eligibility, prepare applications, monitor responses and continuously improve employability.

## 1.2 Primary Objectives

1. Discover relevant job openings without manually visiting numerous websites.
2. Maintain two independent employment pipelines:
   - Jobs in India.
   - International remote jobs accessible to Indian residents.
3. Evaluate opportunities against the latest verified candidate profile and resume.
4. Filter opportunities using configurable suitability thresholds.
5. Present concise, useful information in a centralised dashboard.
6. Maintain a continuously evolving candidate knowledge base.
7. Generate job-specific resumes in DOCX and PDF formats.
8. Track submitted applications and monitor relevant email correspondence.
9. Detect suspicious job postings, emails and system errors.
10. Use AI to perform tasks requiring interpretation and reasoning.
11. Preserve complete user control over external actions.

## 1.3 Non-Objectives

JobHunter will not initially:

- Automatically submit job applications.
- Automatically send emails to recruiters.
- Invent qualifications or professional achievements.
- Guarantee discovery of every job posted online.
- Automatically accept or reject employment offers.
- Replace the user's judgement in career decisions.
- Depend on a paid AI subscription to perform essential functions.

---

# 2. PRODUCT STRUCTURE

The application will contain the following primary sections.

1. Dashboard / Overview
2. India Jobs
3. International Remote Jobs
4. Company Intelligence
5. My Development
6. Resume Studio
7. Application Manager
8. Application Inbox
9. AI Career Assistant
10. Alerts & System Health
11. Settings & Integrations

All sections will operate using a shared candidate profile, centralised database and common application-management system.

---

# 3. DASHBOARD — CENTRAL CONTROL CENTRE

The dashboard should provide a quick understanding of the user's current job-search position.

## 3.1 Information Displayed

- Newly discovered jobs.
- Jobs awaiting review.
- High-match opportunities.
- Active applications.
- Upcoming assessments and interviews.
- Recent email responses.
- Pending follow-ups.
- Skill-development progress.
- Important alerts.
- System integration status.

## 3.2 Dashboard Components

**Opportunity Overview**
- Total matching jobs.
- Newly discovered jobs.
- Jobs awaiting review.
- Jobs shortlisted.
- Applications submitted.

**Application Overview**
- Applications in progress.
- Assessments received.
- Interviews scheduled.
- Offers received.
- Rejections.

**Career Development Overview**
- Recently acquired skills.
- Ongoing learning objectives.
- Projects completed.
- Recommended skills to improve.

**Notifications**
- New high-quality opportunities.
- Application responses.
- Suspicious postings.
- Email warnings.
- Failed synchronisations.

The dashboard must prioritise actionable information rather than decorative statistics.

---

# 4. JOB DISCOVERY ENGINE

This is one of JobHunter's most important subsystems.

## 4.1 Discovery Strategy

The system will use two complementary discovery mechanisms.

### A. Priority Company Discovery

Maintain a dedicated company database containing:

- Company name.
- Industry and category.
- Country and operating locations.
- Official career-page URL.
- Supported job-board integration.
- Target roles.
- Company priority.
- Hiring history.
- Eligibility requirements.
- Notes and referral contacts.

The system should prioritise these companies during scheduled discovery.

### B. Broad Job Discovery

Discover opportunities from supported:

- Company career pages.
- Greenhouse job boards.
- Lever job boards.
- Ashby job boards.
- Public job APIs.
- Remote job boards.
- Other permitted public sources.
- Manually submitted job descriptions and URLs.

Integrations must respect source-specific access restrictions, terms of service and rate limits.

JobHunter must clearly identify the source of every opportunity.

## 4.2 Job Information Extraction

Each discovered opportunity should be converted into a standardised record.

Required fields:

- Job title.
- Company.
- Job description.
- Location.
- Employment type.
- Remote/hybrid/on-site classification.
- Salary range, if available.
- Currency.
- Experience requirements.
- Academic eligibility.
- Graduation-year restrictions.
- Required skills.
- Preferred skills.
- Application deadline.
- Posting date, if available.
- Discovery date.
- Original application URL.
- Source platform.
- Source verification status.

Unavailable information must be marked as unknown rather than fabricated.

## 4.3 Duplicate Detection

JobHunter should identify duplicate postings using:

- Company identity.
- Job title.
- Location.
- External job ID.
- Original URL.
- Similarity of job descriptions.

Repeated discovery of the same opening should update the existing record rather than create unnecessary duplicates.

## 4.4 Job Availability

The system should periodically verify whether saved opportunities remain active.

Possible statuses:

- Active.
- Possibly expired.
- Closed.
- Unavailable.
- Verification failed.

A failed source check must not automatically mean that a position is closed.

---

# 5. TWO INDEPENDENT JOB PIPELINES

## 5.1 Pipeline A — India Jobs

This pipeline targets employment opportunities within India.

Target categories:

- Quantitative trading firms.
- Investment banks.
- Financial institutions.
- Product-based technology companies.
- Fintech companies.
- Global Capability Centres.
- AI and specialised engineering companies.

Filters:

- Company.
- Industry.
- Role.
- Location.
- Salary.
- CGPA.
- Degree requirements.
- Graduation year.
- Experience.
- Skills.
- Application deadline.

## 5.2 Pipeline B — International Remote Jobs

This pipeline targets companies outside India that explicitly permit candidates to work remotely from India.

Target categories:

- US technology startups.
- European technology companies.
- Remote-first organisations.
- International fintech companies.
- Financial technology companies.
- Global engineering teams.

Additional filters:

- Country eligibility.
- India residency acceptance.
- Time-zone requirements.
- Remote restrictions.
- Employment arrangement.
- Contractor versus employee.
- Currency and compensation.
- Experience requirements.

A position labelled remote must not automatically qualify.

The system must distinguish between:
- Remote within one country.
- Remote within a geographic region.
- Remote worldwide.
- Remote with India explicitly supported.

## 5.3 Shared Candidate Profile

Both pipelines will use the same candidate knowledge base but maintain separate:

- Matching thresholds.
- Preferences.
- Application records.
- Analytics.
- Notifications.

---

# 6. JOB EVALUATION AND MATCHING ENGINE

## 6.1 Evaluation Workflow

Whenever a new opportunity is discovered:

1. Extract and standardise the job description.
2. Verify the source and identify authenticity concerns.
3. Retrieve the latest candidate profile.
4. Retrieve the master resume.
5. Extract required and preferred qualifications.
6. Evaluate the candidate against the requirements.
7. Check hard eligibility restrictions.
8. Calculate suitability scores.
9. Apply the configured threshold.
10. Place qualified jobs into the review queue.

## 6.2 Matching Dimensions

Initial proposed scoring model:

| Parameter | Weight |
|---|---:|
| Role relevance | 30% |
| Eligibility | 25% |
| Compensation suitability | 20% |
| Location compatibility | 15% |
| Skills alignment | 10% |

The weights must be configurable.

Hard eligibility failures must be independently enforced. A high aggregate score cannot override a mandatory academic or location restriction.

Unknown eligibility information must be identified separately rather than automatically treated as a pass.

## 6.3 Qualification Thresholds

Initial configuration:

- India Jobs: 75/100.
- International Remote: 80/100.

The user can modify thresholds.

Different thresholds may eventually be configured for:
- Software Engineering.
- Quantitative Development.
- Finance Technology.
- Sales & Trading.
- Other selected roles.

## 6.4 Evaluation Output

Each evaluated opportunity should provide:

**Overall suitability score**

**Strengths**
- Skills that match.
- Relevant projects.
- Relevant experience.
- Matching qualifications.

**Skill gaps**
- Missing mandatory skills.
- Missing preferred skills.
- Experience gaps.
- Knowledge gaps.

**Eligibility**
- Passed.
- Failed.
- Needs verification.

**Recommendation**
- Review.
- Review with caution.
- Below threshold.
- Disqualified.
- Suspicious — quarantined.

Every evaluation should retain its date, model information, scoring version and profile version.

## 6.5 Review Queue

Qualified opportunities enter a dedicated Review Queue.

The user can:

- Open the original job posting.
- View the concise job summary.
- Inspect the full description.
- Review the matching report.
- Save the job.
- Reject the opportunity.
- Shortlist it.
- Generate a tailored resume.

Jobs below the threshold should remain stored in the database for future reassessment.

---

# 7. CANDIDATE INTELLIGENCE AND DEVELOPMENT TRACKING

This subsystem maintains the user's continuously evolving professional profile.

## 7.1 Candidate Profile

The profile will include:

**Academic information**
- College.
- Degree.
- Branch.
- Graduation year.
- CGPA.
- Relevant academic achievements.

**Technical knowledge**
- Programming languages.
- Frameworks.
- Databases.
- Data structures and algorithms.
- Computer science fundamentals.
- Cloud and infrastructure.

**Finance knowledge**
- Financial markets.
- Equity markets.
- Fixed income.
- Derivatives.
- Quantitative finance.
- Valuation.
- Statistics and probability.

**Projects**
- Project title.
- Description.
- Technologies.
- GitHub URL.
- Contributions.
- Achievements.

**Professional experience**
- Internships.
- Employment.
- Certifications.
- Relevant extracurricular experience.

## 7.2 Learning Progress

The user must be able to update progress manually or through AI-assisted interaction.

Each learning record should contain:

- Skill.
- Topic.
- Learning objective.
- Start date.
- Completion date.
- Current status.
- Self-assessed proficiency.
- Practical evidence.
- Related project.
- Verification status.

Possible learning statuses:

- Not started.
- Learning.
- Practising.
- Completed.
- Demonstrated.

## 7.3 Career Knowledge Base

JobHunter must maintain persistent records of professional development.

The system should understand the difference between:

- A topic the user has read about.
- A topic the user has practised.
- A skill the user has demonstrated.
- A skill supported by an actual project or achievement.

AI may suggest profile updates, but the user must approve changes that materially affect the professional profile.

## 7.4 Profile Versioning

Every meaningful profile update should create a historical record.

This allows JobHunter to:
- Re-evaluate older opportunities.
- Track improvements.
- Compare past and current skill profiles.
- Generate historically accurate resumes.
- Identify recurring skill gaps.

---

# 8. RESUME STUDIO

Resume Studio manages all resume-related operations.

## 8.1 Master Resume

The user maintains a master resume containing verified professional information.

This is the source of truth for resume generation.

The master resume must never be overwritten automatically.

## 8.2 Job-Specific Resume Generation

Workflow:

1. Select a shortlisted job.
2. Retrieve its job description.
3. Compare the requirements against the verified candidate profile.
4. Identify relevant experience, projects and skills.
5. Generate a proposed tailored resume.
6. Compare it against the master resume.
7. Highlight modifications.
8. Allow user editing.
9. Obtain approval.
10. Generate DOCX and PDF files.
11. Store the final version against the relevant job and application.

## 8.3 Resume Integrity Rules

AI must never invent:

- Work experience.
- Qualifications.
- Certifications.
- Projects.
- Professional achievements.
- Technical proficiency.
- Quantifiable results.

All generated claims must be traceable to verified profile information or explicitly approved source material.

## 8.4 Resume Library

The library should store:

- Master resume.
- Job-specific resumes.
- Version numbers.
- Creation dates.
- Target company.
- Target job.
- Generated file formats.
- Approval status.
- Change history.

The user should be able to retrieve any previously submitted resume.

---

# 9. APPLICATION MANAGEMENT

## 9.1 Application Workflow

The user applies manually through the original company website.

JobHunter does not submit applications automatically.

The workflow:

1. User reviews the opportunity.
2. User prepares and approves a tailored resume.
3. User opens the original application URL.
4. User completes the application externally.
5. User confirms that the application was submitted.
6. JobHunter records the application.
7. Email monitoring begins.

## 9.2 Application Statuses

- Discovered.
- Under review.
- Shortlisted.
- Preparing application.
- Applied.
- Assessment received.
- Assessment completed.
- Interview scheduled.
- Interview completed.
- Offer received.
- Rejected.
- Withdrawn.
- Closed.

Every status change should have a timestamp and event history.

## 9.3 Application Details

Each application should retain:

- Company.
- Job title.
- Job ID.
- Original posting URL.
- Application date.
- Resume version submitted.
- Referral contact.
- Recruiter details.
- Application status.
- Interview dates.
- Assessment deadlines.
- Notes.
- Email correspondence.
- Follow-up reminders.

---

# 10. APPLICATION INBOX AND EMAIL INTELLIGENCE

## 10.1 Email Integration

Initial integration: Gmail API.

The user may create a dedicated job-search email account.

Use minimum necessary permissions and begin with read-only access.

## 10.2 Email Classification

JobHunter should identify:

- Application acknowledgements.
- Online assessments.
- Interview invitations.
- Interview rescheduling.
- Rejections.
- Offers.
- Recruiter correspondence.
- Follow-up responses.
- Promotional emails.
- Suspicious messages.

## 10.3 Application Matching

Emails should be matched to applications using:

- Company identity.
- Sender domain.
- Job title.
- Job ID.
- Application references.
- Existing correspondence.

If confidence is insufficient, the email must enter a manual review queue.

## 10.4 Notifications

Important messages should generate notifications.

Examples:

- Assessment deadline approaching.
- Interview invitation received.
- Application status updated.
- Follow-up due.
- Suspicious email received.

The system must not assume that a lack of response means rejection.

---

# 11. SECURITY, SCAM DETECTION AND ERROR MANAGEMENT

## 11.1 Job Authenticity

JobHunter should examine:

- Source legitimacy.
- Official company domain.
- Employer identity.
- Posting URL.
- Unusual application requirements.
- Requests for payment.
- Suspicious contact details.
- Inconsistencies in job descriptions.

## 11.2 Email Authenticity

Where available, examine:

- Sender domain.
- SPF, DKIM and DMARC information.
- Domain consistency.
- Suspicious links.
- Unexpected attachments.
- Requests for money or credentials.
- Impersonation indicators.

## 11.3 Quarantine

Suspicious postings and emails should be isolated from normal workflows.

The user must be able to inspect the warning and make a decision.

Automated authenticity assessment is a risk indicator, not a guarantee of safety.

## 11.4 Error Management

Maintain a central error log containing:

- Error ID.
- Timestamp.
- Affected module.
- Severity.
- Description.
- Relevant source or job.
- Retry status.
- Resolution status.

Errors should be visible in the interface rather than silently ignored.

---

# 12. AI ORCHESTRATION

AI should be an interchangeable intelligence layer.

## 12.1 Supported Providers

**Primary cloud provider**
- Google Gemini API.

**Alternative cloud provider**
- GroqCloud, subject to available free quotas.

**Local AI**
- Ollama.
- Initial candidate model: Qwen 2.5 1.5B quantised.

**Future provider**
- OpenAI API, if free credits or an approved budget become available.

Model availability must be configurable.

## 12.2 AI Task Allocation

Use conventional programming wherever deterministic processing is sufficient.

Examples:

| Task | Preferred method |
|---|---|
| Duplicate detection | Python |
| Basic field extraction | Python / local AI |
| Eligibility rules | Python |
| Job description interpretation | Gemini |
| Job suitability assessment | Gemini |
| Resume tailoring | Gemini |
| Email categorisation | Python / local AI |
| Complex career analysis | Cloud AI |
| Notifications | Python |

## 12.3 AI Orchestrator

Responsibilities:

- Task classification.
- Model selection.
- Provider fallback.
- Structured output validation.
- Retry handling.
- Token and quota monitoring.
- Usage tracking.
- Result caching.
- Error reporting.

## 12.4 Zero-Cost Policy

The initial system must not require paid API usage.

Rules:

1. No automatic paid API fallback.
2. Respect provider rate limits.
3. Cache previously processed information.
4. Avoid unnecessary AI calls.
5. Queue tasks when quotas are exhausted.
6. Use local models where appropriate.
7. Allow manual processing if AI is unavailable.
8. Monitor free-tier availability and data policies.

Free-tier quotas and provider terms may change. JobHunter must not depend on permanent access to any specific free model.

Sensitive personal information must not be sent to free cloud providers without appropriate privacy review and explicit user authorisation.

---

# 13. AI CAREER ASSISTANT

A central conversational assistant should allow the user to interact with JobHunter naturally.

Example commands:

- Find new quantitative developer openings.
- Show jobs matching my current profile.
- Why did I fail to qualify for this position?
- What skills am I missing for this job?
- What have I learned in the last month?
- Generate a resume for this position.
- Show all applications awaiting responses.
- Summarise my interview performance.
- Which skills should I study next?

The assistant should retrieve information from JobHunter's database rather than relying on conversation history alone.

All important profile changes must be approved by the user.

---

# 14. UI/UX AND VISUAL DESIGN SPECIFICATION

## 14.1 Overall Design Philosophy

JobHunter must look like a professionally designed productivity and career-management application.

It must not resemble a generic AI-generated SaaS template.

Design references:

- Linear: information hierarchy and navigation.
- Notion: organisation and content presentation.
- Raycast: quick actions and command interface.
- Financial terminals: structured data and dense tables.

These are visual references, not templates to copy.

## 14.2 Visual Principles

- Minimal and professional.
- Clean typography.
- Restrained colour palette.
- Consistent spacing.
- Clear hierarchy.
- High information density without visual clutter.
- Functional icons.
- Subtle borders and shadows.
- Consistent component behaviour.
- Responsive layouts.

Support both light and dark themes.

Avoid:
- Excessive gradients.
- Oversized dashboard cards.
- Decorative AI imagery.
- Unnecessary animations.
- Excessive rounded containers.
- Colourful backgrounds without functional purpose.
- Generic AI-generated website aesthetics.

## 14.3 Navigation

Recommended sidebar:

**JOBHUNTER**
- Overview.
- India Jobs.
- International Remote.
- Review Queue.
- Companies.

**CAREER**
- My Development.
- Resume Studio.
- Applications.
- Application Inbox.

**SYSTEM**
- AI Assistant.
- Alerts.
- Settings.

## 14.4 Job Listing Interface

Job listings should primarily use a structured table.

Recommended columns:

- Company.
- Job title.
- Location.
- Match score.
- Eligibility.
- Salary.
- Date discovered.
- Status.

Selecting a row should open a detailed job panel.

The panel should show:

- Job summary.
- Required skills.
- Candidate strengths.
- Skill gaps.
- Eligibility assessment.
- Authenticity warnings.
- Original application link.
- Available actions.

## 14.5 Review Queue Interface

The review queue should prioritise:

1. High-match opportunities.
2. Upcoming deadlines.
3. Recently discovered jobs.
4. Opportunities with limited application windows.

Use meaningful status indicators rather than decorative badges.

## 14.6 Resume Studio Interface

Use a split-screen editing experience:

- Left: resume content and editing controls.
- Right: document preview.
- Additional panel: job requirements and suggested modifications.

Show differences between the master and tailored resume.

## 14.7 Application Interface

A pipeline or Kanban-style interface can represent application stages.

The user should also have a table view for searching and filtering applications.

## 14.8 General UX Requirements

- Global search.
- Keyboard shortcuts.
- Persistent filters.
- Clear loading states.
- Empty states.
- Error states.
- Confirmation before destructive actions.
- Accessible contrast and typography.
- Responsive behaviour.

---

# 15. TECHNICAL ARCHITECTURE

## 15.1 Architecture Style

Use a modular monolith initially.

Do not introduce microservices unnecessarily.

The application should have logically independent modules that communicate through well-defined interfaces.

## 15.2 Technology Stack

| Component | Technology |
|---|---|
| Frontend | React + TypeScript |
| UI styling | Tailwind CSS |
| UI components | shadcn/ui |
| Backend | Python + FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database migrations | Alembic |
| Background processing | APScheduler initially; Celery + Redis when justified |
| AI | Gemini, Groq and Ollama |
| Email | Gmail API |
| Document generation | python-docx |
| PDF generation | ReportLab or another compatible export pipeline |
| Object storage | Local storage initially; S3-compatible storage later |
| Testing | Pytest + Vitest |
| Version control | Git + GitHub |
| Containerisation | Docker |

Technology choices may be revised when implementation constraints justify doing so.

## 15.3 Main Backend Modules

- Authentication and user management.
- Candidate profile.
- Career development.
- Company management.
- Job discovery.
- Job ingestion.
- Job evaluation.
- Application management.
- Resume generation.
- Email integration.
- AI orchestration.
- Notifications.
- Security and error management.

## 15.4 Database Entities

Initial entities:

- users
- candidate_profiles
- profile_versions
- skills
- career_progress
- skill_evidence
- projects
- companies
- company_roles
- job_sources
- jobs
- job_evaluations
- review_queue
- user_preferences
- applications
- application_events
- application_notes
- contacts
- resume_documents
- resume_versions
- email_accounts
- email_messages
- security_alerts
- approval_requests
- system_errors
- ai_usage_logs
- notifications

Detailed schemas and relationships will be defined in the separate database design document.

---

# 16. SECURITY AND USER CONTROL

JobHunter initially serves one user, but it must still follow sound security practices.

Requirements:

- Secure API credentials.
- Environment variables for secrets.
- No API keys committed to Git.
- Encrypted sensitive data where appropriate.
- Restricted email permissions.
- Secure document access.
- Input validation.
- Protection against malicious job descriptions and prompt injection.
- Source attribution.
- Audit history.
- Database backups.

## 16.1 Approval Policy

The following operations can be automatic:

- Discover jobs.
- Extract job information.
- Evaluate suitability.
- Generate draft resumes.
- Classify emails.
- Create notifications.
- Update verified application information.

The following require explicit user approval:

- Sending applications.
- Sending recruiter emails.
- Replying to correspondence.
- Deleting emails.
- Sharing personal documents.
- Making external commitments.

The approval requirement must be enforced by backend logic.

---

# 17. DEVELOPMENT ROADMAP

Development must follow incremental milestones.

Every milestone should produce a functional, tested component.

## PHASE 0 — PRODUCT AND DESIGN FOUNDATION

Deliverables:

- Final product specification.
- Architecture documentation.
- Database design.
- User journey documentation.
- UI wireframes.
- Design system.
- Development conventions.

Exit criteria:

All major functional requirements and interfaces are documented.

## PHASE 1 — APPLICATION FOUNDATION

Deliverables:

- GitHub repository.
- Frontend project.
- Backend project.
- Database connection.
- Database migrations.
- Environment configuration.
- Basic application navigation.

Exit criteria:

The complete application runs locally and the frontend communicates with the backend.

## PHASE 2 — CANDIDATE PROFILE

Deliverables:

- Candidate profile.
- Academic information.
- Skills.
- Projects.
- Experience.
- Learning progress.
- Profile versioning.

Exit criteria:

The user can maintain and retrieve an evolving professional profile.

## PHASE 3 — JOB MANAGEMENT

Deliverables:

- Company database.
- Priority company watchlist.
- Manual job addition.
- Job listing interface.
- Search and filtering.
- Job detail view.
- Two independent pipelines.

Exit criteria:

The user can manually add and manage opportunities across both pipelines.

## PHASE 4 — AUTOMATED JOB DISCOVERY

Deliverables:

- Greenhouse integration.
- Lever integration.
- Ashby integration.
- Scheduled ingestion.
- Data normalisation.
- Duplicate detection.
- Source tracking.
- Error handling.

Exit criteria:

Supported sources can automatically populate the job database.

## PHASE 5 — JOB INTELLIGENCE

Deliverables:

- Job description analysis.
- Candidate comparison.
- Eligibility engine.
- Suitability scoring.
- Threshold configuration.
- Review queue.
- Evaluation history.

Exit criteria:

New opportunities are automatically evaluated and qualified jobs appear in the review queue.

## PHASE 6 — CAREER INTELLIGENCE

Deliverables:

- Learning history.
- Skill verification.
- Project tracking.
- Profile updates.
- Skill gap analysis.
- Historical progress.

Exit criteria:

Improvements in the user's professional profile influence future job evaluations.

## PHASE 7 — AI INTEGRATION

Deliverables:

- AI orchestrator.
- Gemini integration.
- Groq integration.
- Ollama integration.
- Model routing.
- Structured output validation.
- Caching.
- Usage monitoring.
- Quota handling.

Exit criteria:

AI-powered functionality works within the zero-cost operating policy.

## PHASE 8 — RESUME STUDIO

Deliverables:

- Master resume management.
- Job-specific tailoring.
- Resume comparison.
- User editing.
- DOCX export.
- PDF export.
- Version management.

Exit criteria:

The user can produce and retrieve approved resumes tailored to individual opportunities.

## PHASE 9 — APPLICATION MANAGEMENT

Deliverables:

- Application tracking.
- Application confirmation.
- Status history.
- Interview tracking.
- Follow-up reminders.
- Referral contacts.

Exit criteria:

Every submitted application can be tracked independently.

## PHASE 10 — EMAIL INTELLIGENCE

Deliverables:

- Gmail integration.
- Inbox synchronisation.
- Email classification.
- Application matching.
- Deadline extraction.
- Suspicious email detection.
- Notifications.

Exit criteria:

Relevant application correspondence can be linked to the correct application.

## PHASE 11 — SECURITY AND SYSTEM INTELLIGENCE

Deliverables:

- Suspicious job detection.
- Quarantine.
- Centralised error dashboard.
- Retry handling.
- Approval management.
- Audit history.

Exit criteria:

Suspicious information and system failures are visible and manageable.

## PHASE 12 — FINALISATION AND DEPLOYMENT

Deliverables:

- Complete testing.
- Performance improvements.
- Security review.
- Docker configuration.
- Deployment.
- Database backup procedures.
- Documentation.
- Final user acceptance testing.

Exit criteria:

JobHunter operates reliably as a complete application.

---

# 18. IMPLEMENTATION DOCUMENTATION STRATEGY

This master blueprint is the source of truth for subsequent development.

Individual implementation documents must be created for each milestone.

Recommended documentation structure:

**/docs**

- MASTER_PRODUCT_BLUEPRINT.md
- ARCHITECTURE.md
- DATABASE_DESIGN.md
- UI_UX_DESIGN.md
- API_SPECIFICATION.md
- AI_INTEGRATION_SPECIFICATION.md
- SECURITY_SPECIFICATION.md

**/docs/implementation**

- PHASE_00_FOUNDATION.md
- PHASE_01_APPLICATION_SETUP.md
- PHASE_02_CANDIDATE_PROFILE.md
- PHASE_03_JOB_MANAGEMENT.md
- PHASE_04_JOB_DISCOVERY.md
- PHASE_05_JOB_INTELLIGENCE.md
- PHASE_06_CAREER_INTELLIGENCE.md
- PHASE_07_AI_INTEGRATION.md
- PHASE_08_RESUME_STUDIO.md
- PHASE_09_APPLICATION_MANAGEMENT.md
- PHASE_10_EMAIL_INTELLIGENCE.md
- PHASE_11_SECURITY.md
- PHASE_12_DEPLOYMENT.md

Each implementation document must specify:

1. Objective.
2. Scope.
3. Dependencies.
4. Database changes.
5. Backend implementation.
6. Frontend implementation.
7. API endpoints.
8. AI requirements, if applicable.
9. Error handling.
10. Security considerations.
11. Test cases.
12. Acceptance criteria.
13. Completion checklist.

No milestone should begin without a sufficiently detailed implementation plan.

---

# 19. DEVELOPMENT RULES

These principles are mandatory throughout the project.

1. Build incrementally.
2. Do not write the entire application in one attempt.
3. Maintain clean separation of concerns.
4. Avoid unnecessary complexity.
5. Understand every major implementation decision.
6. Write tests alongside features.
7. Maintain database migrations.
8. Document architectural changes.
9. Commit stable milestones to Git.
10. Never introduce paid dependencies without approval.
11. Never fabricate candidate information.
12. Never silently ignore errors.
13. Preserve data integrity.
14. Maintain user control over external actions.

AI-assisted development must not become blind code generation.

The developer must understand the code, test its behaviour and be able to explain its architecture.

---

# 20. INITIAL ACCEPTANCE VISION

JobHunter will be considered functionally successful when the following complete workflow works:

1. The user creates and maintains a candidate profile.
2. JobHunter discovers an opportunity through an integrated source.
3. The opportunity is assigned to the correct job pipeline.
4. Its authenticity is assessed.
5. Its description is extracted and analysed.
6. It is evaluated against the user's latest verified profile.
7. It passes the configured qualification threshold.
8. It appears in the review queue.
9. The user examines the original job posting.
10. JobHunter generates a proposed tailored resume.
11. The user approves the resume.
12. The user applies manually.
13. The user confirms the application.
14. JobHunter monitors the dedicated inbox.
15. Relevant correspondence is identified.
16. Application status is updated.
17. The user can review the complete application history.

Throughout this workflow, errors must be visible, suspicious activity must be flagged and external actions must remain under user control.

---

# 21. LONG-TERM EXPANSION POSSIBILITIES

These are not initial implementation requirements.

Potential future capabilities:

- Advanced company hiring analytics.
- Recruitment trend analysis.
- Automated referral discovery.
- Interview preparation based on actual job descriptions.
- Interview feedback analysis.
- Salary benchmarking.
- Career progression recommendations.
- More job-source integrations.
- Additional AI providers.
- Mobile-friendly application or mobile app.
- Calendar integration.
- Multi-user support, if the product eventually expands.

These features must not delay the core product.

---

# FINAL PRODUCT STATEMENT

JobHunter is a personal career intelligence system that continuously discovers employment opportunities, evaluates them against an evolving candidate profile, prepares tailored application documents, manages application progress and monitors employer communication.

Its primary value is not merely collecting job listings.

Its value is understanding the relationship between:

- What employers are looking for.
- What the candidate currently offers.
- What the candidate is learning.
- Which opportunities are genuinely accessible.
- What actions need to be taken next.

The platform must remain useful without paid AI services, maintain ownership of its data and preserve complete user control over external actions.

**The ultimate goal is to reduce the manual effort of job searching while improving the quality of career decisions and applications.**

**End of Master Product & Implementation Blueprint — JobHunter v1.0.**