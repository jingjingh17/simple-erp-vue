<template>
    <svg :class="svgClass" aria-hidden="true">
        <use :xlink:href="iconHref"></use>
    </svg>
</template>

<script>
export default {
    name: 'SvgIcon',
    props: {
        iconName: {
            type: String,
            required: true
        },
        svgClass: {
            type: String,
            default: ''
        }
    },
    computed: {
        iconHref() {
            return `#icon-${this.iconName}`;
        }
    }
};
</script>

<style scoped>
svg {
    width: 3em;
    height: 3em;
    fill: currentColor;
}
</style>