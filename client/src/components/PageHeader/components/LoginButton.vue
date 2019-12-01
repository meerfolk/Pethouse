<template>
  <b-button v-bind:disabled="isLoading" @click="onLoginClick">Login</b-button>
</template>

<script>
  export default {
    data: () => ({
      isLoading: false,
    }),
    methods: {
      onLoginClick: function() {
        this.isLoading = true;
        fetch('https://github.com/login/oauth/authorize', {
          method: 'GET',
          redirect: 'follow',
        })
          .then(() => this.isLoading = false);
      },
    },
  }
</script>