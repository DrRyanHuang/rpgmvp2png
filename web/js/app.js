"use strict";

const UI = {
  dropZone: document.getElementById("drop-zone"),
  fileInput: document.getElementById("file"),
  packCheckbox: document.getElementById("pack-files"),
  status: document.getElementById("status"),
  langBtn: document.getElementById("lang-toggle"),
  elementsToTranslate: document.querySelectorAll("[data-i18n]"),
};

const I18N = {
  en: {
    subtitle: "Secure, local-only decryption for your RPG Maker MV assets.",
    dropText: "Click to browse or drag files here",
    zipLabel: "Download as ZIP archive",
    githubLink: "View on GitHub",
    noFiles: "No valid .rpgmvp files found.",
    processing: "Processing {count} files...",
    success: "Successfully converted {count} files!",
    errorGeneric: "An error occurred. Check console for details.",
    fileTooSmall: "File too small to be a valid RPGMVP file.",
    btnText: "中文",
  },
  zh: {
    subtitle: "安全、本地化的 RPG Maker MV 素材解密工具。",
    dropText: "点击选择或拖拽文件至此",
    zipLabel: "打包下载为 ZIP",
    githubLink: "查看 GitHub 仓库",
    noFiles: "未找到有效的 .rpgmvp 文件。",
    processing: "正在处理 {count} 个文件...",
    success: "成功转换 {count} 个文件！",
    errorGeneric: "发生错误，请查看控制台详情。",
    fileTooSmall: "文件太小，不是有效的 RPGMVP 文件。",
    btnText: "English",
  },
};

let currentLang = "en";

// Initialize event listeners
document.addEventListener("DOMContentLoaded", () => {
  UI.fileInput.addEventListener("change", handleFileSelect);
  UI.langBtn.addEventListener("click", toggleLanguage);

  // Drag and drop support
  ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
    UI.dropZone.addEventListener(eventName, preventDefaults, false);
  });

  ["dragenter", "dragover"].forEach((eventName) => {
    UI.dropZone.addEventListener(eventName, highlight, false);
  });

  ["dragleave", "drop"].forEach((eventName) => {
    UI.dropZone.addEventListener(eventName, unhighlight, false);
  });

  UI.dropZone.addEventListener("drop", handleDrop, false);
  
  // Detect browser language
  const browserLang = navigator.language.startsWith("zh") ? "zh" : "en";
  setLanguage(browserLang);
});

function toggleLanguage() {
  setLanguage(currentLang === "en" ? "zh" : "en");
}

function setLanguage(lang) {
  currentLang = lang;
  document.documentElement.lang = lang;
  UI.langBtn.textContent = I18N[lang].btnText;

  UI.elementsToTranslate.forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (I18N[lang][key]) {
      el.textContent = I18N[lang][key];
    }
  });
}

function t(key, params = {}) {
  let text = I18N[currentLang][key] || key;
  for (const [k, v] of Object.entries(params)) {
    text = text.replace(`{${k}}`, v);
  }
  return text;
}

function preventDefaults(e) {
  e.preventDefault();
  e.stopPropagation();
}

function highlight() {
  UI.dropZone.querySelector(".upload-label").classList.add("dragover");
}

function unhighlight() {
  UI.dropZone.querySelector(".upload-label").classList.remove("dragover");
}

function handleDrop(e) {
  const dt = e.dataTransfer;
  const files = dt.files;
  processFiles(files);
}

function handleFileSelect(event) {
  const files = event.target.files;
  processFiles(files);
  // Reset input so same file can be selected again
  event.target.value = "";
}

async function processFiles(files) {
  if (!files || files.length === 0) return;

  const validFiles = Array.from(files).filter((f) =>
    f.name.toLowerCase().endsWith(".rpgmvp")
  );

  if (validFiles.length === 0) {
    showStatus(t("noFiles"), "error");
    return;
  }

  showStatus(t("processing", { count: validFiles.length }), "processing");

  try {
    const shouldPack = UI.packCheckbox.checked;

    if (shouldPack) {
      await processAndPackFiles(validFiles);
    } else {
      await processFilesIndividually(validFiles);
    }
    
    showStatus(t("success", { count: validFiles.length }), "success");
  } catch (error) {
    console.error(error);
    showStatus(t("errorGeneric"), "error");
  }
}

async function processAndPackFiles(files) {
  const zip = new JSZip();
  const promises = files.map(async (file) => {
    const pngData = await decryptRPGMVPFile(file);
    const fileName = file.name.replace(/\.rpgmvp$/i, ".png");
    zip.file(fileName, pngData);
  });

  await Promise.all(promises);
  
  const content = await zip.generateAsync({ type: "blob" });
  downloadBlob(content, "converted_images.zip");
}

async function processFilesIndividually(files) {
  for (const file of files) {
    const pngData = await decryptRPGMVPFile(file);
    const blob = new Blob([pngData], { type: "image/png" });
    const fileName = file.name.replace(/\.rpgmvp$/i, ".png");
    downloadBlob(blob, fileName);
  }
}

function decryptRPGMVPFile(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const data = new Uint8Array(e.target.result);
      // PNG Header: 89 50 4E 47 0D 0A 1A 0A
      const pngHeader = new Uint8Array([
        0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d,
        0x49, 0x48, 0x44, 0x52,
      ]);

      if (data.length < 32) {
        reject(new Error(t("fileTooSmall")));
        return;
      }

      const pngData = new Uint8Array(pngHeader.length + data.length - 32);
      pngData.set(pngHeader);
      pngData.set(data.slice(32), pngHeader.length);
      resolve(pngData);
    };
    reader.onerror = () => reject(reader.error);
    reader.readAsArrayBuffer(file);
  });
}

function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
}

function showStatus(message, type) {
  UI.status.textContent = message;
  UI.status.className = `status-message ${type}`;
  
  // Auto-hide success message after 3 seconds
  if (type === "success") {
    setTimeout(() => {
        UI.status.classList.add("hidden");
    }, 3000);
  }
}
