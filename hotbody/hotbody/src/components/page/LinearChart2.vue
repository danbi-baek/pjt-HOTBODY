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
                    labels: [
                        '9월',
                        '10월',
                        '11월',
                        '12월',
                        '1월',
                        '2월',
                     
                    ],
                    datasets: [
                        {
                            label: '체지방률',
                            fill:false,
                            borderWidth: 3,
                            borderColor:'rgb(255, 88, 102)',
                            pointBackgroundColor:'rgb(255, 88, 102)',
                            pointBorderWidth:4,
                            //Data to be represented on y-axis
                            data: [
                                40,
                                23,
                                18,
                                14,
                                13,
                                8,
                                
                            ]
                        },
                        {
                            label: 'BMI',
                            fill:false,
                            borderWidth: 3,
                            borderColor:'#5765FF',
                            pointBackgroundColor:'#5765FF',
                            pointBorderWidth:4,
                            //Data to be represented on y-axis
                            data: [
                                24,
                                20,
                                19,
                                14,
                                12,
                                10,
                                
                            ]
                        },
                         {
                            label: '근육량',
                            fill:false,
                            borderWidth: 3,
                            borderColor:'#66FF57',
                            pointBackgroundColor:'#66FF57',
                            pointBorderWidth:4,
                            //Data to be represented on y-axis
                            data: [
                                10,
                                20,
                                19,
                                24,
                                25,
                                30,
                                
                            ]
                        },
                    ]
                },
                //Chart.js options that controls the appearance of the chart
                options: {
                    tooltips: {
                    },
                    hover: {
                    },
                    scales: {
                        yAxes: [
                            {
                                ticks: {
                                    beginAtZero: true,
                                    display: true,
                                    maxTicksLimit: 8
                                },
                                gridLines: {
                                    display: false
                                }
                            }
                        ],
                        xAxes: [
                            {
                                ticks: {
                                    // display: false,
                                    padding:-380,
                                   // fontSize: 15
                                },
                                gridLines: {
                                    display: true
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