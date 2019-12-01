const fetchMock = require('fetch-mock');

module.exports = story => {
  fetchMock.reset();
  return story();
}
