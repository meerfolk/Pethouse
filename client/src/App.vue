<template>
  <page-header/>
</template>

<script>
  import PageHeader from './components/PageHeader/PageHeader';
  import AppStore from './AppStore';

  export default {
    components: {
      'page-header': PageHeader,
    },
    store: AppStore,
    mounted() {
      this.$store.dispatch('getConfig');
    },
  }
</script>>