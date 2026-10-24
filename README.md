# MiCompress for Flow Launcher

Compress **images, PDFs, video, audio, documents & archives** right from
[Flow Launcher](https://www.flowlauncher.com), powered by
[micompress.com](https://micompress.com/?utm_source=flow-launcher&utm_medium=plugin&utm_campaign=extend).

## Usage

```
mc C:\Users\me\Pictures\photo.jpg
```

Type `mc` followed by a file path (Explorer's *Copy as path* works — quotes are stripped), pick a preset
(**Recommended**, **Lossless** or **Extreme**) and press Enter. An optimized `photo-min.jpg` is written next
to the original; the original file is never modified.

## Install

From Flow Launcher: `pm install MiCompress`

## How it works

The selected file is uploaded over HTTPS to micompress.com, compressed there, and the result is downloaded
back. No account is needed within the anonymous size limits. Uploaded files are deleted from the server
automatically — see the [privacy policy](https://micompress.com/privacy).

Supported formats include JPG, PNG, WebP, GIF, AVIF, HEIC, TIFF, SVG, RAW, PDF, MP4, MOV, MP3, WAV, DOCX,
XLSX, PPTX, EPUB, ZIP, 7Z and more.

## License

MIT © [MiCompress](https://micompress.com)
