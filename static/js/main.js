

// 取得主繪製區塊
const chart1 = echarts.init(document.getElementById('main'));
const chart2 = echarts.init(document.getElementById('acc'));
// const chart3 = echarts.init(document.getElementById('coms'));

window.onresize = function () {
    chart1.resize();
    chart2.resize();
};

// select選擇option時的監聽
// $("#select_company").change(() => {
//     com = $("#select_company").val();
//     console.log(com);
// });

// function drawComEPS(com) {
//     chart3.showLoading();
//     $.ajax(
//         {
//             url: `/com-EPS-data/${com}`,
//             type: "GET",
//             dataType: "json",
//             success: (result) => {
//                 // 繪製對應區塊並給予必要參數
//                 drawChat(chart3, com, "各券商營收資料", result["acc_company"], acc_result["acc_current_EPS"])
//                 chart3.hideLoading();
//             },
//             error: () => {
//                 alert("資料讀取失敗，請洽佩宜!")
//                 chart3.hideLoading();
//             }
//         }
//     )
// }





// 呼叫後端資料跟繪製
// 繪製累計EPS
drawAccEPS();
function drawAccEPS() {
    chart2.showLoading();
    $.ajax(
        {
            url: "/acc-EPS-data",
            type: "GET",
            dataType: "json",
            success: (acc_result) => {
                this.setTimeout(() => {
                    $("#acc_eps_high_company").text(acc_result["acc_highest"]["acc_company"]);
                    $("#acc_eps_high_value").text(acc_result["acc_highest"]["acc_current_EPS"]);
                    $("#acc_eps_high_rank").text(acc_result["acc_highest"]["acc_current_rank"]);

                    $("#acc_eps_second_company").text(acc_result["acc_second"]["acc_company"]);
                    $("#acc_eps_second_value").text(acc_result["acc_second"]["acc_current_EPS"]);
                    $("#acc_eps_second_rank").text(acc_result["acc_second"]["acc_current_rank"]);

                    // 本公司
                    $("#acc_eps_point_company").text(acc_result["acc_point"]["acc_company"]);
                    $("#acc_eps_point_value").text(acc_result["acc_point"]["acc_current_EPS"]);
                    $("#acc_eps_point_rank").text(acc_result["acc_point"]["acc_current_rank"]);

                    // 繪製對應區塊並給予必要參數
                    drawChat(chart2, "累計EPS", "累計稅後EPS", acc_result["acc_company"], acc_result["acc_current_EPS"], "#40E0D0")
                    chart2.hideLoading();
                }, 1000);
            },
            error: () => {
                alert("資料讀取失敗，請洽佩宜!")
                chart2.hideLoading();
            }
        }
    )
}



// 取得後端資料
// 繪製當月EPS
drawEPS();
function drawEPS() {
    chart1.showLoading();
    $.ajax(
        {
            url: "/current-EPS-data",
            type: "GET",
            dataType: "json",
            success: (result) => {
                this.setTimeout(() => {
                    $("#eps_high_company").text(result["highest"]["company"]);
                    $("#eps_high_value").text(result["highest"]["current_EPS"]);
                    $("#eps_high_rank").text(result["highest"]["current_rank"]);

                    $("#eps_second_company").text(result["second"]["company"]);
                    $("#eps_second_value").text(result["second"]["current_EPS"]);
                    $("#eps_second_rank").text(result["second"]["current_rank"]);

                    // 本公司
                    $("#eps_point_company").text(result["point"]["company"]);
                    $("#eps_point_value").text(result["point"]["current_EPS"]);
                    $("#eps_point_rank").text(result["point"]["current_rank"]);

                    // 繪製對應區塊並給予必要參數
                    drawChat(chart1, "當月EPS", "本月稅後EPS", result["company"], result["current_EPS"])
                    chart1.hideLoading();
                }, 1000);
            },
            error: () => {
                alert("資料讀取失敗，請洽佩宜!")
                chart1.hideLoading();
            }
        }
    )
}


function drawChat(chart, title, legend, xData, yData, color = '#87CEEB') {
    // 指定圖表的配置項目和數據
    let option = {
        title: {
            text: title
        },
        tooltip: {},
        legend: {
            data: [legend]
        },
        xAxis: {
            data: xData
        },
        yAxis: {},
        series: [
            {
                name: legend,
                type: 'bar',
                data: yData,
                itemStyle: {
                    normal: {
                        color: function (params) {
                            if (params.name === "統一證券") {
                                return "#FFDEAD";
                            } else {
                                return color;
                            }
                        }
                    }
                }
            }
        ]
    };

    // 使用 chart.setOption(option) 來設置圖表配置
    chart.setOption(option);
}








