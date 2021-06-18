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
                    labels:this.$store.state.chartlabels,
                    datasets: [
                        {
                            label: 'BMI',
                            backgroundColor: 'rgb(255, 88, 102)',
                            pointBackgroundColor: 'rgb(255, 88, 102)',
                            borderWidth: 3,
                            pointRadius:8,
                            pointHoverRadius:6,
                            pointBorderColor:'white',
                            pointBorderWidth:4,
                            hoverBackgroundColor:'white',
                            //Data to be represented on y-axis
                            data:this.$store.state.chartdatas
                        }
                    ]
                },
                //Chart.js options that controls the appearance of the chart
                options: {
                    tooltips: {
                    },
                    hover: {
                        animationDuration: 0
                    },

                    animation: { // 데이터 항상 표시
                        duration: 1,
                        onComplete: function () {
                            var chartInstance = this.chart,
                                ctx = chartInstance.ctx;
                            ctx.fillStyle = 'white';
                            ctx.textAlign = 'right';
                            ctx.textBaseline = 'bottom';
                            this
                                .data
                                .datasets
                                .forEach(function (dataset, i) {
                                    var meta = chartInstance
                                        .controller
                                        .getDatasetMeta(i);
                                    meta
                                        .data
                                        .forEach(function (bar, index) {
                                            var data = dataset.data[index];
                                            ctx.fillText(data, bar._model.x, bar._model.y - 5);
                                        });
                                });

                            
                        }
                    },
                    scales: {
                        yAxes: [
                            {
                                ticks: {
                                    beginAtZero: true,
                                    display: false,
                                    maxTicksLimit: 10,
                                    max: 100
                                },
                                gridLines: {
                                    display: true,
                                    color:'white'
                                }
                            }
                        ],
                        xAxes: [
                            {
                                ticks: {
                                    display: true,
                                    padding:-410,
                                    fontColor:'white',
                                //    fontSize: 15
                                },
                                gridLines: {
                                    display: true,
                                    color:'white'

                                },
                                
                            }
                        ]
                    },
                    legend: {
                        display: false,
                    },
                    responsive: true,
                    maintainAspectRatio: false
                }
            }
        },
        mounted() {
            this.renderChart(this.datacollection, this.options)
        }
    }
</script>