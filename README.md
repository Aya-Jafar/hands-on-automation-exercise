# The Truth About Automation – When, Why, and How
## Hands-on Lab Automation Exercise: 
### A Simple Python App that needs automation
---
#### Step 1 (Execrcise)
- Fork the App Repo

- Create .github/workflows/deploy.yml

- Add the code of the Github action to automate:

- The test of this application.

- Configure a server of your choice (i.e. DigitalOcean) and deploy the application.
    - i.e. we have seen a similar example before (slides 19 & 20)
---
#### Step 2 (Enhancements You Can Add):

- ✅ Pre-commit hooks for linting and formatting
- ✅ Coverage reporting using tools like [coverage.py](https://coverage.readthedocs.io/en/7.9.1/)
- ✅ Slack or email alerts on success/failure
- ✅ Matrix builds for Python 3.8, 3.9, 3.10
- ✅ Separate staging & production environments
- ✅ Automated rollback if deployment fails
