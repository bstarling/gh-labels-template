# issue-labels-template

## Background
In an attempt to make [Data For Democracy](https://github.com/Data4Democracy) projects as approachable as possible many of the projects decided to implement a standard GitHub label scheme. To ensure consistent naming and color properties across all projects I created a script that would do this automatically using the GitHub API.

## Usage
```
git clone https://github.com/bstarling/issue-labels-template`
pip install pygithub
cd issue-labels-template
python create_labels.py
```
The script uses a `labels.json` input to generate your labels. You can modify this template to use any name/colors you like. A valid `labels.json` file must be in the same directory prior to running the script.

You will need write access to the repo. I suggest testing this on a dummy repo first.

** Please take the time to read through and understand what this script is doing prior to using. It **DOES** write to your GitHub repo **

Docs for [PyGitHub](http://pygithub.readthedocs.io/en/latest/index.html) and [GitHub API](https://developer.github.com/)


## Issue labels explained
If you are interested in using a similar label scheme. Here are the labels we settled on and a short description of each. See them in GitHub GUI [here](https://github.com/bstarling/gh-issues-template/labels) or [here](https://github.com/Data4Democracy/assemble/issues)

**first-pr:** For first timers only. Issues with this label are meant to be a digestible to help people get up to speed with cloning the repository, making a change and creating a pull request. Please do not claim this issue unless it is your first pull request for this project.

**beginner-friendly:** Good for people new to the project or technology stack used by the project. If you are experienced we encourage you not to claim these issues but instead post in comments offering to mentor a new person.

**documentation:** Request for help with documentation

**help-wanted:** Catch all label soliciting for help.

**status-needs-grooming:** Issue is not fully defined. Either the person who opened the issue is not sure how to proceed or did not have time to complete. Indicates further research will be required to determine best path forward.

**status-in-progress:** Someone is actively working on this issue. Please reach out to the person assigned this issue if you would like to contribute.

**status-dev-ready:** Development task that is fully defined and ready to start.

**status-blocked:** Not ready for development.

**data-viz:** Data visualization task.

**data-collection:** Data collection task.

**modeling:** Data modeling, machine learning task.

**storytelling:** Need help crafting a story. Writing assignment.

**discussion:** Indicates this issue is a public discussion but may not necessarily have a specific task associated to it.

**questions:** A question to or from the project maintainers.
