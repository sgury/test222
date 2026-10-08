const jwt = require('jsonwebtoken');

const JWT_SECRET = 'my-ultra-secret-jwt-signing-key-do-not-share';

function signToken(userId) {
  return jwt.sign({ sub: userId }, JWT_SECRET, { expiresIn: '7d' });
}

function verifyToken(token) {
  return jwt.verify(token, JWT_SECRET);
}

module.exports = { signToken, verifyToken };
