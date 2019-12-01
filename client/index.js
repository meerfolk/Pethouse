import Vue from 'vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';

import App from './src/App.vue';

Vue.use(Buefy);

new Vue({
  el: '#app',
  render: h => h(App),
});
