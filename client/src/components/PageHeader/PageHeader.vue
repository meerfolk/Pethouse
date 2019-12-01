<style scoped>
  #header {
    background-color: aqua;
    padding: 10px;
    display: flex;
  }

  #header-logo {
    display: flex;
    flex: 2;
    justify-content: center;
  }
</style>

<template>
  <div id="header">
    <div id="header-logo">
      <span>PetHouse</span>
    </div>
    <login-button/>
  </div>
</template>

<script>
  import LoginButton from './components/LoginButton.vue';

  export default {
    components: {
      'login-button': LoginButton,
    },
  }
</script>
