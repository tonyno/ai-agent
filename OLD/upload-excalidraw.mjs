import { readFileSync } from 'node:fs';
import { webcrypto } from 'node:crypto';

const filePath = process.argv[2];
if (!filePath) {
  console.error('Usage: node upload-excalidraw.mjs <path-to-.excalidraw>');
  process.exit(1);
}

const json = readFileSync(filePath, 'utf8');
const data = new TextEncoder().encode(json);

const key = await webcrypto.subtle.generateKey(
  { name: 'AES-GCM', length: 128 },
  true,
  ['encrypt', 'decrypt'],
);

const iv = webcrypto.getRandomValues(new Uint8Array(12));
const ciphertext = await webcrypto.subtle.encrypt({ name: 'AES-GCM', iv }, key, data);

const payload = new Uint8Array(iv.length + ciphertext.byteLength);
payload.set(iv, 0);
payload.set(new Uint8Array(ciphertext), iv.length);

const res = await fetch('https://json.excalidraw.com/api/v2/post/', {
  method: 'POST',
  body: payload,
});

if (!res.ok) {
  console.error('Upload failed:', res.status, await res.text());
  process.exit(1);
}

const body = await res.json();
const id = body.id ?? body.data?.id;
if (!id) {
  console.error('Unexpected response:', JSON.stringify(body));
  process.exit(1);
}

const jwk = await webcrypto.subtle.exportKey('jwk', key);
console.log(`https://excalidraw.com/#json=${id},${jwk.k}`);
