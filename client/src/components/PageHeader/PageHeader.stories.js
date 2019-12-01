import Vue from 'vue';
import PageHeader from './PageHeader.vue';
import fetchMock from 'fetch-mock';
import { storiesOf } from '@storybook/vue';

import BaseDecorator from '../../../storybook/lib/BaseDecorator';

Vue.component('page-header', PageHeader);


function timeout(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

storiesOf('PageHeader', module).addDecorator(BaseDecorator).add('Base', () => {
  fetchMock.get('https://github.com/login/oauth/authorize', async (url, { body }) => {
    await timeout(1000);
    return { test: 'test' };
  });

  return '<page-header/>'
});
