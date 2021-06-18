<template>
    <div class="linearGauage">
          <!-- <div>바디 분석</div> -->
          <div class="chart">
            <highcharts-vue class="highcharts" :options="chartOptions1" :highcharts="hcInstance"> 
            </highcharts-vue>
            <!-- 체지방량, 근육량, bmi, bmr,dayKcal(하루권장칼로리) -->
          <!-- 체지방량 
            남자 - 30세 이전 :  
            -->
          </div>
    </div>
</template>

<script>
import Highcharts from 'highcharts'
import {Chart} from 'highcharts-vue'
export default {
  components: {
    HighchartsVue: Chart,
  },
  data(){
    return{
      hcInstance: Highcharts,
      chartOptions1:{
        chart: {
        type: "bar",
        //height:100,
        margin: [55, 15, 55, 15],
        plotBorderWidth: 0
        //plotBorderColor: '#999',
      },
      credits: { enabled: false },
      exporting: { enabled: false },
      legend: { enabled: false },
      title: {
        text: "The 5 stages of chronic kidney disease (CKD)"
      },
      xAxis: {
        tickLength: 0,
        lineWidth: 0,
        title: { text: "Good" }
      },
      yAxis: {
        min: 0,
        tickColor: "#888",
        tickWidth: 1,
        tickLength: 6,
        //tickInterval:15,
        tickPositions: [0, 15, 30, 45, 60, 90, 120],
        //minorTickInterval:5,
        //minorTickWidth:2,
        //minorTickLength:4,
        minorGridLineWidth: 0,
        tickPosition: "outside",
        gridLineWidth: 2,
        endOnTick: true,
        title: {
          text: "Your eGFR is 90",
          style: { fontSize: "16px", fontWeight: "bold", color: "#000" },
          useHTML: true
        }
      },

      plotOptions: {
        series: {
          animation: false,
          enableMouseTracking: false,
          marker: {
            enabled: true,
            fillColor: "#000000",
            symbol: "diamond",
            radius: 8,
            color: "#000000"
            //symbol:
            //"url(https://icons.veryicon.com/png/o/object/material-design-icons-1/rhombus-2.png)",
            //width: 35,
            //height: 35,
          },
          bar: {},
          scatter: {}
        }
      }
          }
        }

  },
  methods:{
    
  },
  mounted(){
 

  }
}

</script>
<style lang="scss" scoped>
.linearGauage{
  // border: 1px solid red;
  width: 99%;
  height: 1000pxpx;

}
.chart{
  height: 400px;
}
.highcharts{
  width: 100%;
  // height: 20%;
}


body {
  font-family: helvetica, sans-serif;
  font-size: 0.7em;
}
p {
  margin: 0.5em 1em;
}
.plotlabel {
  margin-top: 30%;
  font-weight: bold;
  font-size: 14px;
  color: #000;
}
</style>