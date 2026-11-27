# 发布到GitHub

建议仓库名：`amazon-market-research`。

建议描述：`An eight-stage Amazon market research skill with evidence checks, product tagging, competitor analysis and CPA modeling.`

建议主题：`ai-workflow`、`codex-skill`、`amazon`、`market-research`、`product-management`。

## 网页上传

1. 登录自己的GitHub账号，创建同名仓库，选择公开可见（适合简历展示）。仓库根目录应直接包含本项目的README.md，不要只上传ZIP。
2. 解压项目发布包，将内部文件及目录上传，保留 `skills/`、`docs/`、`examples/`、`scripts/` 结构。
3. 使用有意义的提交说明，例如 `Add eight-stage market research skill and portfolio documentation`。
4. 打开仓库首页，确认README显示、相对链接可打开、技能文件完整，再将实际仓库链接放到简历。

具体入口参见[GitHub创建仓库说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)及[上传文件说明](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)。

## 本地Git发布

此目录可作为独立Git仓库。创建远端空仓库后，在本地仓库终端配置本人认可的提交身份（可用GitHub提供的隐私邮箱），然后执行：

```powershell
git add .
git commit -m "Add market research skill and portfolio documentation"
git remote add origin https://github.com/YOUR_USERNAME/amazon-market-research.git
git push -u origin main
```

把 `YOUR_USERNAME` 替换为真实用户名。若origin已存在，先查看其目标，不要覆盖未知远端。Git身份设置和GitHub登录是两件不同的事；通过GitHub登录流程完成认证，不要把令牌写进命令、项目文件或聊天。

## 发布范围

本项目不包含真实业务原始数据、个人账号信息或旧评论分析项目的虚拟环境。请勿上传运行中产生的市场报告或账号配置。许可证由作者决定，当前发布包没有附加许可证。GitHub公开展示不自动代表已采用开源许可证。

发布成功后再使用“已发布GitHub”的简历描述；本地包准备完成不等于线上发布完成。
