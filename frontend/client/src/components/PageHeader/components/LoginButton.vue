<template>
  <a v-bind:href="githubHref">
    <b-button v-bind:disabled="isDisabled">Login</b-button>
  </a>
</template>

<script>
  import AppStore from '../../../AppStore';

  export default {
    store: AppStore,
    computed: {
      isDisabled() {
        return !Boolean(this.$store.state.config);
      },
      githubHref() {
        let clientId;
        let redirectUri;

        if (this.$store.state.config && this.$store.state.config.github) {
          ({ client_id: clientId, redirect_uri: redirectUri } = this.$store.state.config.github);
        }
        if (clientId && redirectUri) {
          return `https://github.com/login/oauth/authorize?client_id=${clientId}&redirect_uri=${redirectUri}`;
        }
      },
    },
  }
</script>