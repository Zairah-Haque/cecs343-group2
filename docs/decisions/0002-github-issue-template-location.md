Decision: Keep slice.md in .github/ISSUE_TEMPLATE/ so GitHub can offer it when someone creates an issue.

Rejected alternatives:
- Put slice.md at the repository root. This was the alternative named in Prompt D; GitHub does not use a root-level file as an issue template.
- Put slice.md in docs/. GitHub’s issue-template behavior depends on its recognized template location, which the team cannot change.
Costs: Contributors need to know that the template lives under .github/ISSUE_TEMPLATE/; moving it elsewhere would change whether GitHub offers it during issue creation.
