function getRandomNumber(min, max) {
    const num = Math.floor(Math.random() * (max - min + 1)) + min;
    return num;
  }

// ======= GRAFICO IMC GERAL =======

var options_geral = {
    series: [{
    name: 'Abaixo do peso',
    data: [44, 55, 41, 37, 22, 43, 21]
  }, {
    name: 'Peso Normal',
    data: [53, 32, 33, 52, 13, 43, 32]
  }, {
    name: 'Sobrepeso',
    data: [12, 17, 11, 1, 15, 11, 20]
  }, {
    name: 'Obesidade',
    data: [9, 7, 5, 8, 6, 9, 4]
  }],
    chart: {
    type: 'bar',
    height: 350,
    stacked: true,
  },
  plotOptions: {
    bar: {
      horizontal: true,
      dataLabels: {
        total: {
          enabled: true,
          offsetX: 0,
          style: {
            fontSize: '12px',
            fontWeight: 600
          }
        }
      }
    },
  },
  stroke: {
    width: 1,
    colors: ['#fff']
  },
  title: {
    text: 'IMC Infantil Geral'
  },
  xaxis: {
    categories: ['7º ano', '6º ano', '5º ano', '4º ano', '3º ano', '2º ano', '1º ano'],
    labels: {
      formatter: function (val) {
        return val 
      }
    }
  },
  yaxis: {
    title: {
      text: undefined
    },
  },
  tooltip: {
    y: {
      formatter: function (val) {
        return val 
      }
    }
  },
  fill: {
    opacity: 1
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left',
    offsetX: 40
  }
  };




// ======= GRAFICO IMC FEMININO=======

var options_female = {
    series: [{
    name: 'Abaixo do peso',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }, {
    name: 'Peso Normal',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }, {
    name: 'Sobrepeso',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }, {
    name: 'Obesidade',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }],
    chart: {
    type: 'bar',
    height: 350,
    stacked: true,
  },
  plotOptions: {
    bar: {
      horizontal: true,
      dataLabels: {
        total: {
          enabled: true,
          offsetX: 0,
          style: {
            fontSize: '12px',
            fontWeight: 600
          }
        }
      }
    },
  },
  stroke: {
    width: 1,
    colors: ['#fff']
  },
  title: {
    text: 'IMC Infantil Feminino'
  },
  xaxis: {
    categories: ['7º ano', '6º ano', '5º ano', '4º ano', '3º ano', '2º ano', '1º ano'],
    labels: {
      formatter: function (val) {
        return val 
      }
    }
  },
  yaxis: {
    title: {
      text: undefined
    },
  },
  tooltip: {
    y: {
      formatter: function (val) {
        return val 
      }
    }
  },
  fill: {
    opacity: 1
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left',
    offsetX: 40
  }
  };


// ======= GRAFICO IMC MASCULINO =======

var options_male = {
    series: [{
    name: 'Abaixo do peso',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }, {
    name: 'Peso Normal',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }, {
    name: 'Sobrepeso',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }, {
    name: 'Obesidade',
    data: [getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10), getRandomNumber(1,10)]
  }],
    chart: {
    type: 'bar',
    height: 350,
    stacked: true,
  },
  plotOptions: {
    bar: {
      horizontal: true,
      columnWidth: '55%',
      borderRadiusApplication: 'end',
      borderRadiusWhenStacked: 'last',
      borderRadius: '12',
      dataLabels: {
        total: {
          enabled: true,
          offsetX: 0,
          style: {
            fontSize: '12px',
            fontWeight: 600
          }
        }
      }
    },
  },
  stroke: {
    show: true,
    width: 2,
    colors: ['transparent']
  },
  title: {
    text: 'IMC Infantil Masculino'
  },
  xaxis: {
    categories: ['7º ano', '6º ano', '5º ano', '4º ano', '3º ano', '2º ano', '1º ano'],
    labels: {
      formatter: function (val) {
        return val 
      }
    }
  },
  yaxis: {
    title: {
      text: undefined
    },
  },
  tooltip: {
    theme:'dark',
    y: {
      formatter: function (val) {
        return val 
      }
    }
  },
  fill: {
    type: 'gradient',
  gradient: {
    shade: 'dark',
    type: "vertical",
    shadeIntensity: 0.3,
    gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
    inverseColors: false,
    opacityFrom: 1,
    opacityTo: 0.95,
    stops: [0, 100],
    colorStops: []
  }
  },
  legend: {
    position: 'top',
    horizontalAlign: 'left',
    offsetX: 40
  }
  };


// ============ GRAFICO DONNUT ===============

var options = {
  plotOptions: {
    pie: {
      donut: {
        labels: {
          show: true,
          name: {
            show: true,
            fontWeight: 600
          },
          value: {
            show: true,
            formatter: function (val) {
              return val + "%"
            },
            fontWeight: 600
          }
        }
      }
    }
  },
    series: [44, 55],
    labels: ['IMC Normal', 'IMC fora do padrão'],
    chart: {
    type: 'donut',
    width: '300px',
    height: '345px'
    
  },
  dataLabels: {
    enabled: true
  },
  legend: {
    position:'bottom'
  },
  responsive: [{
    breakpoint: 1599,
    options: {
      chart: {
        width: 300
      },
      legend: {
        position:'bottom'
      }
    }
  }]
  };

  var chart2 = new ApexCharts(document.querySelector("#chart-2"), options);
  chart2.render();


 var chart = new ApexCharts(document.querySelector("#geral"), options_geral);
 chart.render();


 var chart = new ApexCharts(document.querySelector("#female"), options_female);
 chart.render();

 var chart = new ApexCharts(document.querySelector("#male"), options_male);
 chart.render();

 