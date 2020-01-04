import Vue from 'vue';
import App from './App.vue';
import { storiesOf } from '@storybook/vue';
import { action } from '@storybook/addon-actions';
import fetchMock from 'fetch-mock';

import BaseDecorator from '../storybook/lib/BaseDecorator';

Vue.component('app', App);

function timeout(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

storiesOf('App', module).addDecorator(BaseDecorator).add('Base', () => {
  fetchMock.get(new RegExp('/api/config'), async () => {
    action('GET CONFIG');
    await timeout(2000);
    return {
      github: {
        client_id: 'example_client_id',
        redirect_uri: 'example_redirect_uri',
      },
    };
  });

  return '<app/>'
});
