import Vue from 'vue';
import PageHeader from './PageHeader.vue';
import { storiesOf } from '@storybook/vue';

import BaseDecorator from '../../../storybook/lib/BaseDecorator';
import AppStore from '../../AppStore';

Vue.component('page-header', PageHeader);

storiesOf('PageHeader', module).addDecorator(BaseDecorator).add('Base', () => {
  AppStore.commit('setConfig', {
    github: {
      client_id: 'test_client_id',
      redirect_uri: 'test_redirect_uri',
    },
  });

  return '<page-header/>'
});
