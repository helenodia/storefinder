<template>
  <section class="store-finder__container">
    <SearchForm />
  </section>
</template>

<script>
import SearchForm from './SearchForm.vue';

export default {
  name: 'StoreFinder',
  components: {
    SearchForm
  }
}
</script>
