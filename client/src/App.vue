<template>
  <div class="app-container">
    <Header />
    <StoreFinder />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import StoreFinder from './components/StoreFinder.vue';

export default {
  name: 'App',
  components: {
    Header,
    StoreFinder
  }
}
</script>

<style scoped lang="css">
@import './assets/css/global.css';
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@700&display=swap');
@font-face {
  font-family: 'Labil Grotesk Black';
  src: local('Labil Grotesk Black'),
  url(./assets/fonts/LabilGrotesk/LabilGroteskTrial-Black.otf) format('truetype');
}
</style>
