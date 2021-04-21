<template>
  <div class="store-card__container">
    <div class="store-card__">
      <h3 class="store-card__heading">{{ store.name }}</h3>
      <p>{{ store.postcode }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StoreCard',
  props: ['store']
}
</script>
