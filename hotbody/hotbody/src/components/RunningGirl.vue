<template>
<div class="css_lab">

    <input type="radio" id="stop" name="action"/>
    <input type="radio" id="run" name="action" checked="checked"/>
    <input type="radio" id="walk" name="action"/>

    <input type="radio" id="type1" name="color"/>
    <input type="radio" id="type2" name="color" checked="checked"/>
    <input type="radio" id="type3" name="color"/>

    <input type="radio" id="slow" name="speed"/>
    <input type="radio" id="normal" name="speed" checked="checked"/>
    <input type="radio" id="fast" name="speed"/>

    <div class="woman">
        <label for="stop"></label>
        <label for="run"></label>
        <div class="head">
            <p></p>
            <p></p>
            <p></p>
            <p></p>
            <p></p>
            <p></p>
        </div>
        <div class="body">
            <p></p>
            <p></p>
            <p></p>
        </div>
        <div class="r_arm">
            <p></p>
            <p>
                <span></span>
            </p>
        </div>
        <div class="l_arm">
            <p></p>
            <p>
                <span></span>
            </p>
        </div>
        <div class="r_foot">
            <p></p>
            <p>
                <span>
                    <strong></strong>
                    <em></em>
                </span>
            </p>
        </div>
        <div class="l_foot">
            <p></p>
            <p>
                <span>
                    <strong></strong>
                    <em></em>
                </span>
            </p>
        </div>
    </div>

    <div class="road">
        <p></p>
        <p></p>
        <p></p>
    </div>
</div>
</template>

<script>
export default {

}
</script>

<style scoped>
@import '../assets/css/RunningGirl.css';
</style>