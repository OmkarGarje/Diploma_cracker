# GitHub Repository Setup Instructions

## Step 1: Create Repository on GitHub

1. Go to [GitHub.com](https://github.com) and sign in to your account
2. Click the **"+"** button in the top-right corner
3. Select **"New repository"**
4. Fill in the repository details:
   - **Repository name**: `Diploma_cracker`
   - **Description**: `Educational platform designed to help diploma students excel in their academics`
   - **Visibility**: Choose **Public** (so it can be used with GitHub Pages)
   - **DO NOT** check "Initialize this repository with a README" (we already have files)
   - **DO NOT** add .gitignore or license (we already have these)
5. Click **"Create repository"**

## Step 2: Connect Your Local Repository

After creating the repository, GitHub will show you commands to push your existing repository. You should run these commands in PowerShell from the project directory:

```powershell
# Navigate to your project directory (if not already there)
Set-Location "D:\omkar\omkar\diploma-cracker-github-pages"

# Add the remote repository (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/Diploma_cracker.git

# Push your code to GitHub
git push -u origin main
```

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (in the repository navigation)
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select **"Deploy from a branch"**
5. Choose **"main"** branch
6. Choose **"/ (root)"** folder
7. Click **Save**

## Step 4: Access Your Live Website

After a few minutes, your website will be live at:
```
https://YOUR_USERNAME.github.io/Diploma_cracker/
```

## Current Repository Status

✅ **Local Git repository**: Initialized and ready
✅ **All files committed**: 32 files successfully committed
✅ **Branch**: Set to 'main' (GitHub's default)
✅ **Files included**:
- HTML pages (index.html, coding.html, theory.html, etc.)
- CSS stylesheets (organized in css/ folder)
- Images (organized in images/ folder) 
- PowerPoint presentations (organized in assets/ folder)
- Documentation (README.md, DEPLOYMENT.md)
- Configuration (.gitignore)

## What to Replace

When you see `YOUR_USERNAME` in the commands above, replace it with your actual GitHub username: **OmkarGarje**

So your commands will be:
```powershell
git remote add origin https://github.com/OmkarGarje/Diploma_cracker.git
git push -u origin main
```

And your live website will be at:
```
https://omkargarje.github.io/Diploma_cracker/
```

## Troubleshooting

If you encounter any issues:
1. Make sure you're signed in to GitHub
2. Ensure the repository name matches exactly: `Diploma_cracker`
3. Check that the repository is set to Public
4. Verify you're in the correct directory when running Git commands

## Next Steps After Setup

Once your repository is created and code is pushed:
1. Check that all files are visible in your GitHub repository
2. Enable GitHub Pages as described above
3. Wait a few minutes for the site to deploy
4. Visit your live website URL
5. Share the link with your fellow students!

---

**Your Diploma Cracker project is ready to go live! 🚀**