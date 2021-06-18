function saveNicknameToCookie(value) {
  document.cookie = `nickname=${value}`;
}

function saveEmailToCookie(value) {
  document.cookie = `email=${value}`;
}

function saveTokenToCookie(value) {
  document.cookie = `token=${value}`;
}

function saveUserpkToCookie(value) {
  document.cookie = `userpk=${value}`;
}

function saveHeightToCookie(value) {
  document.cookie = `height=${value}`;
}

function saveWeightToCookie(value) {
  document.cookie = `weight=${value}`;
}

function getNicknameFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)nickname\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getEmailFromCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)email\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getTokenToCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)token\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getUserpkToCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)userpk\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getHeightToCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)height\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function getWeightToCookie() {
  return document.cookie.replace(
    /(?:(?:^|.*;\s*)weight\s*=\s*([^;]*).*$)|^.*$/,
    '$1',
  );
}

function deleteCookie(value) {
  document.cookie = `${value}=; expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}


export {
  saveNicknameToCookie,
  saveEmailToCookie,
  saveTokenToCookie,
  saveUserpkToCookie,
  saveHeightToCookie,
  saveWeightToCookie,
  getNicknameFromCookie,
  getEmailFromCookie,
  getTokenToCookie,
  getUserpkToCookie,
  getHeightToCookie,
  getWeightToCookie,
  deleteCookie,
};

