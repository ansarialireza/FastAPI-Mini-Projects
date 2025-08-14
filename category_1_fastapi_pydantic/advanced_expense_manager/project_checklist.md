# Project Checklist – 5 Phases of Software Development

---

## Phase 1 – Planning & Design (20–30% time)

- [x] Review project description and extract **feature list**
- [x] Define **project goal** (1-2 sentences)
- [x] Design **API routes table** (Method, URL, Description, Request, Response, Status Codes)
- [x] Design **folder/file structure** (Architecture)
- [x] Specify initial **dependencies** and create `requirements.txt`
- [ ] Identify **edge cases** (invalid input, errors, special conditions)
- [ ] (For DB projects) Draw **ER diagram** and define relationships
- [x] Document all above in `notes.md`

---

## Phase 2 – Implementation (40–50% time)

- [ ] Initialize Git repository or project folder
- [ ] Create initial branch (e.g. `feature/setup`)
- [ ] Install dependencies and update `requirements.txt`
- [ ] Step-by-step implementation:
  - [ ] Models (Pydantic / SQLAlchemy)
  - [ ] API routes
  - [ ] Validation and error handling
- [ ] Commit with meaningful messages after each major step (e.g. `feat: add task creation endpoint`)
- [ ] Follow clean code practices (PEP8, black, flake8)
- [ ] Run and manually test each endpoint after creation

---

## Phase 3 – Testing & Debugging (15–20% time)

- [ ] Write simple **unit tests** with pytest for main features
- [ ] Manual testing with Postman / Thunder Client
- [ ] Test **edge cases** (empty inputs, non-existent items, etc.)
- [ ] Debug errors using `pdb` or print statements
- [ ] Log errors and fixes in `notes.md`

---

## Phase 4 – Deployment & Optimization (10–15% time)

- [ ] Run project locally with `uvicorn` or similar
- [ ] Check `/docs` auto-generated docs and fix bugs
- [ ] Refactor and optimize code (async, remove duplicates, etc.)
- [ ] Add environment variables if needed
- [ ] Push code to GitHub
- [ ] (Optional) Setup Docker or CI/CD pipeline for advanced projects

---

## Phase 5 – Review & Documentation (10% time)

- [ ] Write **retrospective**:
  - What did I learn?
  - What challenges did I face?
  - What improvements can be made?
- [ ] Complete `README.md` (install, run, test, brief project explanation)
- [ ] Final commit and push to GitHub
- [ ] Log project details in overall `learning_log.md`

---

*Use this checklist for every mini-project to keep your development process consistent and professional.*
