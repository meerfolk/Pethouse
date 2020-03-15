import { configure  } from "@storybook/vue";
import Vue from 'vue';
import Buefy from 'buefy';

import 'buefy/dist/buefy.css'

Vue.use(Buefy);

configure(require.context('../src', true, /\.stories\.js$/), module);
