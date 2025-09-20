# GitHub Pages Deployment Guide

This guide will help you deploy your Diploma Cracker project to GitHub Pages for free hosting.

## 📋 Prerequisites

- A GitHub account
- Git installed on your computer
- Your project files ready (which we've already organized!)

## 🚀 Step-by-Step Deployment Instructions

### Step 1: Create a New Repository on GitHub

1. Go to [GitHub.com](https://github.com)
2. Click the **"+"** button in the top-right corner
3. Select **"New repository"**
4. Name your repository: `diploma-cracker-github-pages` (or any name you prefer)
5. Make sure it's set to **Public**
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click **"Create repository"**

### Step 2: Initialize Git in Your Project Folder

Open PowerShell/Terminal in the `diploma-cracker-github-pages` folder and run:

```bash
git init
git add .
git commit -m "Initial commit: Diploma Cracker project setup"
```

### Step 3: Connect to GitHub Repository

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/diploma-cracker-github-pages.git
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** (in the repository menu)
3. Scroll down to **Pages** in the left sidebar
4. Under **Source**, select **"Deploy from a branch"**
5. Choose **"main"** branch
6. Choose **"/ (root)"** folder
7. Click **Save**

### Step 5: Access Your Website

After a few minutes, your website will be available at:
```
https://YOUR_USERNAME.github.io/diploma-cracker-github-pages/
```

## 📝 Making Updates

To update your website:

1. Make changes to your files locally
2. Run these commands:
   ```bash
   git add .
   git commit -m "Update: describe your changes"
   git push
   ```
3. Changes will appear on your live site within a few minutes

## 🔧 Troubleshooting

### Common Issues:

**Issue**: Website shows 404 error
- **Solution**: Make sure your main HTML file is named `index.html`
- **Solution**: Check that GitHub Pages is enabled in repository settings

**Issue**: CSS/Images not loading
- **Solution**: Verify all paths in HTML files use relative paths (like `css/style.css`, `images/photo.jpg`)
- **Solution**: Make sure file names match exactly (case-sensitive)

**Issue**: PowerPoint files not downloading
- **Solution**: GitHub has file size limits. Large files might need to be hosted elsewhere or compressed

### File Size Limitations:
- Individual files: Max 100MB
- Repository: Max 1GB
- If PowerPoint files are too large, consider compressing them or using external hosting

## 📞 Support

If you encounter issues:
1. Check the GitHub Pages documentation
2. Verify all file paths are correct
3. Make sure your repository is public
4. Contact the development team through their GitHub profiles

## 🎯 Optional Enhancements

### Custom Domain (Optional)
If you want to use a custom domain like `diplomacracker.com`:
1. Buy a domain from a registrar
2. In your repository, add a file named `CNAME` containing your domain
3. Configure DNS settings with your domain provider

### SEO Optimization (Optional)
- Add meta descriptions to each HTML page
- Include structured data for better search engine visibility
- Add social media meta tags for better sharing

### Analytics (Optional)
- Add Google Analytics to track visitor statistics
- Use GitHub's built-in traffic analytics

---

**🎓 Your Diploma Cracker project is now ready for the world to see!**

*Made with ❤️ by TYCM-1 Students | Bharati Vidyapeeth Institute of Technology, Navi Mumbai*