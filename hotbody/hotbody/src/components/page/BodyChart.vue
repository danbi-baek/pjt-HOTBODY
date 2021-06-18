<script>
    //Importing Line class from the vue-chartjs wrapper
    import {Line} from 'vue-chartjs'
    //Exporting this so it can be used in other components
    export default {
        extends: Line,
        data() {
            return {
                datacollection: {
                    //Data to be represented on x-axis
                    labels: this.$store.state.chartDate,
                    datasets: [
                        {
                            label: '체지방률',
                            fill:false,
                            borderWidth: 3,
                            borderColor:'rgb(255, 88, 102)',
                            pointBackgroundColor:'rgb(255, 88, 102)',
                            pointBorderWidth:4,
                            //Data to be represented on y-axis
                            data: this.$store.state.chartFat
                        },
                        {
                            label: '몸무게',
                            fill:false,
                            borderWidth: 3,
                            borderColor:'#5765FF',
                            pointBackgroundColor:'#5765FF',
                            pointBorderWidth:4,
                            //Data to be represented on y-axis
                            data: this.$store.state.chartWeight
                        },
                    ]
                },
                //Chart.js options that controls the appearance of the chart
                options: {
                    elements:{
                        line:{
                            tension : 0,
                        }

                    },
                    tooltips: {
                    },
                    hover: {
                    },
                    scales: {
                        yAxes: [
                            {
                                ticks: {
                                    max: 90,
                                    beginAtZero: true,
                                    display: true,
                                    // maxTicksLimit: 8
                                },
                                gridLines: {
                                    // display: false
                                }
                            }
                        ],
                        xAxes: [
                            {
                                ticks: {
                                    display: false,
                                    // padding:-380,
                                   // fontSize: 15
                                },
                                gridLines: {
                                    // display: true
                                },
                                
                            }
                        ]
                    },
                    legend: {
                        position:'bottom',
                        align:'end',
                        labels:{
                            boxWidth:10,
                            padding:20
                        }
                    },
                    maintainAspectRatio: false,
                }
            }
        },
        mounted() {
            this.renderChart(this.datacollection, this.options)
        }
    }
</script>