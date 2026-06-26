<!-- source: qwen-mapdownload — https://raw.githubusercontent.com/Hxy1992/MapDownload/main/QWEN.md -->
# QWEN.md - MapDownload 项目上下文

## 项目概述

**MapDownload** 是一个基于 **Electron + Vue 3 + Vite** 的桌面应用程序，用于下载多种在线地图的瓦片数据。

### 核心功能

- 支持多种地图源：高德地图、百度地图（含自定义地图）、腾讯地图、OpenStreetMap、CartoDb、ArcGIS 在线地图、天地图、MapBox
- 支持卫星遥感影像和标注合并
- 支持行政区划瓦片下载，裁切边界
- 支持下载瓦片格式：jpeg、png、webp
- 下载任务支持暂停、恢复、取消，支持失败任务重试和管理
- 使用 maptalks 在应用内预览地图

### 技术栈

| 类别 | 技术 |
|------|------|
| 框架 | Electron 16 |
| 前端 | Vue 3.2 + Vue Router 4 |
| UI 库 | Naive UI |
| 构建工具 | Vite 2 |
| 地图库 | maptalks |
| 地理计算 | @turf/* |
| 图像处理 | sharp |
| 网络请求 | superagent |
| 代码规范 | ESLint |

### 项目架构

```
MapDownload/
├── packages/
│   ├── main/          # Electron 主进程（Node.js 后端逻辑）
│   │   ├── src/
│   │   │   ├── index.js          # 主进程入口
│   │   │   ├── ipcMain.js        # IPC 通信处理
│   │   │   ├── ipHandle.js       # IP 处理
│   │   │   └── downloadWorker.js # 下载工作线程
│   │   └── vite.config.js
│   ├── preload/       # Electron 预加载脚本
│   │   ├── src/
│   │   └── vite.config.js
│   └── renderer/      # 渲染进程（前端 UI）
│       ├── src/
│       │   ├── components/       # Vue 组件
│       │   ├── cesium-helper/    # Cesium 集成辅助代码
│       │   ├── geojson/          # GeoJSON 数据
│       │   ├── use/              # Vue composables
│       │   ├── utils/            # 工具函数
│       │   ├── style/            # 样式文件
│       │   ├── App.vue
│       │   ├── index.js          # 渲染进程入口
│       │   └── router.js         # 路由配置
│       ├── index.html
│       └── vite.config.js
├── scripts/           # 构建脚本
├── tests/             # 测试文件
├── buildResources/    # 应用构建资源（图标等）
└── .electron-builder.config.js  # Electron Builder 配置
```

## 开发与构建命令

```bash
# 安装依赖
npm install

# 开发模式（热更新）
npm run dev
# 或
npm run watch

# 构建前端资源
npm run build

# 构建 Electron 应用（开发模式，不打包 asar）
npm run compile

# 代码检查
npm run lint

# 运行测试
npm run test
```

## 开发约定

### 代码风格

- 使用 ESLint 进行代码检查，配置基于 `eslint:recommended`
- 必须使用分号（`semi: error`）
- 多行结构推荐使用尾随逗号（`comma-dangle: warn`）
- 使用单引号（`quotes: warn`）
- 检查范围：`.js`, `.ts`, `.vue` 文件

### 路径别名

- 渲染进程中使用 `/@/` 作为 `packages/renderer/src/` 的别名
- 主进程中使用 `/@/` 作为 `packages/main/src/` 的别名

### 构建流程

1. Vite 分别打包 main、preload、renderer 三个模块
2. main 和 preload 输出为 CommonJS 格式（`.cjs`）
3. renderer 输出为浏览器可用格式
4. Electron Builder 将构建结果打包为桌面应用

### 目标平台

- 浏览器目标：Chrome 96
- Node.js 版本：>= 16.13
- npm 版本：>= 8.1

## 主要组件说明

| 组件 | 说明 |
|------|------|
| Home.vue | 主页，地图下载核心界面 |
| AreaChoose.vue | 区域选择组件 |
| LayerControl.vue | 图层控制组件 |
| ProgressControl.vue | 下载进度控制组件 |
| Save.vue | 保存配置组件 |
| FailedRecordsDialog.vue | 失败任务管理对话框 |
| Help.vue | 帮助页面 |
| About.vue | 关于页面 |

## 注意事项

- 本项目仅供个人学习与科研使用
- 下载的瓦片数据版权归地图服务商所有
- 百度个性化地图（午夜蓝、清新蓝、黑夜等）链接已失效
