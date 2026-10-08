const jwt = require('jsonwebtoken');

const JWT_ALGORITHM = 'HS256';
const JWT_SECRET = process.env.JWT_SECRET;

if (!JWT_SECRET) {
  throw new Error('JWT_SECRET environment variable is not set');
}

function signToken(userId) {
  if (userId === undefined || userId === null || userId === '') {
    throw new Error('signToken: userId is required');
  }
  // jsonwebtoken requires "sub" to be a string; numeric IDs would throw.
  return jwt.sign({ sub: String(userId) }, JWT_SECRET, {
    algorithm: JWT_ALGORITHM,
    expiresIn: '7d',
  });
}

// Throws (TokenExpiredError / JsonWebTokenError) on invalid tokens — callers must catch.
function verifyToken(token) {
  if (typeof token !== 'string' || token.length === 0) {
    throw new jwt.JsonWebTokenError('jwt must be provided');
  }
  // Pin the algorithm to prevent algorithm-confusion attacks.
  return jwt.verify(token, JWT_SECRET, { algorithms: [JWT_ALGORITHM] });
}

module.exports = { signToken, verifyToken };
