// Catatan: untuk Node.js terbaru, kita perlu menggunakan import atau CommonJS fetch
// Kita akan menggunakan versi dengan CommonJS

// Perhatikan juga kita mungkin perlu menginstall node-fetch dulu:
// npm install node-fetch@2

const fetch = require('node-fetch');

async function testLogin() {
  try {
    console.log('Mencoba login ke http://127.0.0.1:5000/api/auth/login...');
    
    const response = await fetch('http://127.0.0.1:5000/api/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: 'Tasya',
        password: 'capstone01'
      }),
    });
    
    console.log('Status response:', response.status);
    const data = await response.json();
    console.log('Response data:', data);
    
    if (data.access_token) {
      console.log('Login berhasil! Token diterima.');
    } else {
      console.log('Login gagal. Periksa pesan error.');
    }
    
    return data;
  } catch (error) {
    console.error('Error saat mencoba login:', error);
  }
}

testLogin();