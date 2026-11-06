# GitHub upload instructions

## Create the repository

Create an empty GitHub repository, for example `hand-tracking-snake-game`. It may be Public or Private. Do not ask GitHub to add a README, `.gitignore`, or license because this folder already contains them.

From this folder, run:

```bash
git init -b main
git add .
git status
git commit -m "Prepare hand-tracking Snake game"
git remote add origin https://github.com/YOUR_USERNAME/hand-tracking-snake-game.git
git remote -v
git push -u origin main
```

Replace `YOUR_USERNAME` with the GitHub account name. If GitHub requests a password for an HTTPS push, use an appropriately scoped personal access token instead of the account password, and never paste the token into screenshots or chat.

## Final check before pushing

- Confirm that `git status` does not list the demonstration video.
- Do not force-add ignored `.mp4` files.
- Add only consented, privacy-checked screenshots in the future.
- Check the GitHub file list after pushing and confirm that `LICENSE` is detected as MIT.

