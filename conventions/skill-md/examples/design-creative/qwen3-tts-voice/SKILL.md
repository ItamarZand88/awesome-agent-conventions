<!-- source: qwen3-tts-voice — https://raw.githubusercontent.com/mu-zi-lee/qwen3-tts-skill/main/SKILL.md -->
---
name: qwen3-tts-skills
description: 围绕 Qwen3-TTS 提供本地 TTS 工作流。支持：单句语音生成（CustomVoice/VoiceDesign/VoiceClone）、长文稿批量配音生成（文章→配音稿JSON→批量TTS→合并）。适用场景：生成语音、有声书配音、视频旁白、多角色对话朗读、语音克隆。
---

# Qwen3-TTS 技能

将文本转换为高质量语音的完整工作流。

## 🚀 快速开始

### 场景 1：单句语音生成

直接调用脚本生成语音：

```bash
# 中文语音（默认 Vivian 女声）
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py custom-voice \
  --language Chinese \
  --text "你好，欢迎使用语音合成。" \
  --out-dir outputs

# 英文语音（默认 Ryan 男声）
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py custom-voice \
  --language English \
  --text "Hello, welcome to text-to-speech." \
  --out-dir outputs
```

### 场景 2：长文稿批量配音

将文章转换为完整语音文件：

```
用户文稿 → [AI分析生成配音稿] → [用户审核] → [批量TTS] → 完整语音.wav
```

详见下方 **[长文稿批量配音](#-长文稿批量配音生成)** 章节。

---

## 📋 模型选择指南

根据需求选择合适的模型：

| 模式 | 模型 | 适用场景 | 命令 |
|------|------|----------|------|
| **CustomVoice** | `Qwen3-TTS-12Hz-1.7B-CustomVoice` | 使用内置音色 + 情感控制 | `custom-voice` |
| **VoiceDesign** | `Qwen3-TTS-12Hz-1.7B-VoiceDesign` | 用自然语言描述想要的音色 | `voice-design` |
| **VoiceClone** | `Qwen3-TTS-12Hz-1.7B-Base` | 克隆参考音频的声音 | `voice-clone` |
| **Tokenizer** | `Qwen3-TTS-Tokenizer-12Hz` | 音频编解码 | `tokenizer-roundtrip` |

### 内置 Speaker（CustomVoice 模式）

| 语言 | 默认 Speaker | 说明 |
|------|-------------|------|
| Chinese | Vivian | 女声，自然 |
| English | Ryan | 男声 |
| Japanese | Ono_Anna | 女声 |
| Korean | Sohee | 女声 |

---

## 🎙️ 单句语音生成

### CustomVoice（推荐入门）

使用内置音色，可选情感控制：

```bash
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py custom-voice \
  --language Chinese \
  --text "其实我真的有发现，我是一个特别善于观察别人情绪的人。" \
  --speaker Vivian \
  --instruct "轻松愉快的语气" \
  --out-dir outputs
```

**参数说明**：
- `--language`：Chinese / English / Japanese / Korean
- `--speaker`：可选，不填则按语言自动选默认
- `--instruct`：可选，情感/语气控制（如"开心地说"、"低沉缓慢"）
- `--output`：可选，指定输出文件名（默认自动生成时间戳文件名）

### VoiceDesign（设计独特音色）

用自然语言描述想要的音色：

```bash
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py voice-design \
  --language Chinese \
  --text "哥哥，你回来啦，人家等了你好久好久了，要抱抱！" \
  --instruct "体现撒娇稚嫩的萝莉女声，音调偏高且起伏明显。" \
  --out-dir outputs
```

**注意**：VoiceDesign 的 `--instruct` 是**必填**的，用于描述音色特征。

### VoiceClone（语音克隆）

克隆参考音频的声音：

```bash
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py voice-clone \
  --language English \
  --ref-audio "path/to/reference.wav" \
  --ref-text "参考音频的文本内容" \
  --text "要合成的新文本" \
  --out-dir outputs
```

**参数说明**：
- `--ref-audio`：参考音频文件路径或 URL
- `--ref-text`：参考音频对应的文本（必填）
- `--x-vector-only-mode`：可选，仅使用说话人特征（质量可能降低）

**⚠️ 注意**：VoiceClone 不支持 `--instruct` 情感控制。

### Tokenizer（音频编解码）

用于音频的编码和解码验证：

```bash
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py tokenizer-roundtrip \
  --audio "path/to/audio.wav" \
  --out-dir outputs
```

---

## 🎬 长文稿批量配音生成

将长文章、剧本、有声书内容转换为完整语音文件。

### 工作流程

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Step 1         │     │  Step 2         │     │  Step 3         │     │  输出           │
│  AI分析文稿     │ ──→ │  用户审核修改   │ ──→ │  批量生成语音   │ ──→ │  完整语音.wav   │
│  生成配音稿JSON │     │  保存.json文件  │     │  FFmpeg合并     │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘     └─────────────────┘
```

### Step 1：让 AI 生成配音稿

向 AI 说：*"把下面这篇文章转成语音"* + 贴上文章内容

AI 会按 `dubbing-skills/SKILL.md` 的规则：
1. 智能切分（每段 200-300 字）
2. 识别角色（`【旁白】`、`【小明】` 等）
3. 分析情感，生成 `instruct`
4. 输出配音稿 JSON

### Step 2：用户审核修改

检查 JSON 并调整：
- 切分是否合理
- 角色分配是否正确
- 情感 `instruct` 是否合适
- TTS 模式是否需要调整

保存为 `article.dubbing.json` 文件。

### Step 3：批量生成语音

```bash
uv run qwen3-tts-skills/scripts/batch_dubbing.py \
  --input article.dubbing.json \
  --out-dir outputs
```

**参数说明**：

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input` | 配音稿 JSON 文件 | 必填 |
| `--out-dir` | 输出目录 | outputs |
| `--silence-gap` | 普通段落间静音（秒）| 0.3 |
| `--character-switch-gap` | 角色切换时静音（秒）| 0.5 |
| `--clean-segments` | 合并后删除中间片段 | 保留 |

### 输出结构

```
outputs/
├── segments/
│   ├── seg_001_旁白.wav
│   ├── seg_002_小明.wav
│   └── ...
├── article.dubbing.json   # 配音稿备份
└── article_final.wav      # 最终完整语音
```

### 支持的三种模式

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| `custom-voice` | 内置音色 + 情感指令 | 大多数场景（默认）|
| `voice-design` | 自然语言描述音色 | 需要特定音色（萝莉、大叔等）|
| `voice-clone` | 克隆参考音频 | 需要真人/特定人声音 |

---

## 🔧 环境配置

### 推荐方式：直接用 uv run

脚本内已声明依赖，无需手动安装：

```bash
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py -h
```

### 创建固定虚拟环境

```bash
uv venv --python 3.12
.\.venv\Scripts\activate
uv pip install -U qwen-tts
```

### 安装 FlashAttention 2（可选，降低显存）

```bash
uv pip install -U flash-attn --no-build-isolation

# 内存 < 96GB 时限制并行任务
MAX_JOBS=4 uv pip install -U flash-attn --no-build-isolation
```

**使用条件**：
- 硬件兼容 FlashAttention 2
- 模型以 `torch.float16` 或 `torch.bfloat16` 加载

### 安装 FFmpeg（批量配音必需）

Windows：
```powershell
choco install ffmpeg -y
```

验证安装：
```bash
ffmpeg -version
```

---

## 📥 模型离线下载

### 使用 ModelScope（中国大陆推荐）

```bash
uv pip install -U modelscope
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --local_dir ./Qwen3-TTS-12Hz-1.7B-CustomVoice
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign --local_dir ./Qwen3-TTS-12Hz-1.7B-VoiceDesign
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-Base --local_dir ./Qwen3-TTS-12Hz-1.7B-Base
modelscope download --model Qwen/Qwen3-TTS-Tokenizer-12Hz --local_dir ./Qwen3-TTS-Tokenizer-12Hz
```

### 使用 Hugging Face

```bash
uv pip install -U "huggingface_hub[cli]"
huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --local-dir ./Qwen3-TTS-12Hz-1.7B-CustomVoice
huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign --local-dir ./Qwen3-TTS-12Hz-1.7B-VoiceDesign
huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-Base --local-dir ./Qwen3-TTS-12Hz-1.7B-Base
huggingface-cli download Qwen/Qwen3-TTS-Tokenizer-12Hz --local-dir ./Qwen3-TTS-Tokenizer-12Hz
```

---

## 🖥️ 本地 Web UI 演示

```bash
# 查看帮助
qwen-tts-demo --help

# 启动 CustomVoice
qwen-tts-demo Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --ip 0.0.0.0 --port 8000

# 启动 VoiceDesign
qwen-tts-demo Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign --ip 0.0.0.0 --port 8000
```

### HTTPS 支持（解决麦克风权限问题）

```bash
# 生成自签名证书
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

# 启用 HTTPS
qwen-tts-demo Qwen/Qwen3-TTS-12Hz-1.7B-Base \
  --ip 0.0.0.0 --port 8000 \
  --ssl-certfile cert.pem \
  --ssl-keyfile key.pem \
  --no-ssl-verify
```

---

## 📚 参考文档

| 文档 | 说明 |
|------|------|
| `dubbing-skills/SKILL.md` | 配音稿生成规范（AI 阅读用） |
| `dubbing-skills/references/dubbing_format.md` | 配音稿 JSON 格式详细规范 |
| `dubbing-skills/references/examples.md` | 各种场景的配音稿示例 |
| `references/python_api.md` | Python API 集成指南 |

---

## ⚡ 性能参数

```bash
uv run qwen3-tts-skills/scripts/run_qwen3_tts.py custom-voice \
  --device-map cuda:0 \
  --dtype bfloat16 \
  --attn flash_attention_2 \
  --language Chinese \
  --text "测试文本" \
  --out-dir outputs
```

| 参数 | 说明 |
|------|------|
| `--device-map` | 指定 GPU（如 `cuda:0`）或 CPU |
| `--dtype` | 数据类型：auto / bfloat16 / float16 / float32 |
| `--attn` | 注意力实现：auto / flash_attention_2 |

---

## ❓ 常见问题

### Windows 路径问题

绝对路径需要用双引号包裹：

```bash
uv run "C:/Users/lee/.config/alma/skills/qwen3-tts-skills/scripts/run_qwen3_tts.py" -h
```

### SoX 警告

如果看到 `SoX could not be found!`，安装 SoX（不影响功能，只是消除警告）：

```powershell
choco install sox.portable -y
```

### 模型下载慢

优先使用 ModelScope（中国大陆）或提前下载到本地目录。
