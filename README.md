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

## API key (optional)

Small files work without an account. For bigger files and a monthly allowance, paste your personal API key
(`mc_…`, shown on your [account page](https://micompress.com/account) — creating an account is free) into
**Settings → Plugins → MiCompress → API key**. Alternatively set the `MICOMPRESS_API_KEY` environment variable;
the plugin setting wins if both are present.

| Plan | Compressions per month | Notes |
|------|------------------------|-------|
| No key (anonymous) | Anonymous limits | Small files only |
| Free account | 50 via the API | Files up to 100 MB |
| Plus ($9.99/mo) | 1,000 | Shared with website usage |
| Pro ($19.99/mo) | 5,000 | Shared with website usage |

When the allowance is used up the plugin shows the server's quota message with a link to
[micompress.com/plans](https://micompress.com/plans).

## How it works

The selected file is uploaded over HTTPS to micompress.com, compressed there, and the result is downloaded
back. No account is needed within the anonymous size limits. Uploaded files are deleted from the server
automatically — see the [privacy policy](https://micompress.com/privacy).

Supported formats include JPG, PNG, WebP, GIF, AVIF, HEIC, TIFF, SVG, RAW, PDF, MP4, MOV, MP3, WAV, DOCX,
XLSX, PPTX, EPUB, ZIP, 7Z and more.

## License

MIT © [MiCompress](https://micompress.com)
