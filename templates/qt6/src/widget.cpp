#include "widget.hpp"
#include "./ui_widget.h"

Widget::Widget(QWidget *parent) : QWidget(parent), ui(new Ui::Widget)
{
    ui->setupUi(this);

    connect(ui->countButton, &QPushButton::clicked, [=]() {
        counter++;
        ui->incrementLabel->setText(QString::number(counter));
    });
}

Widget::~Widget()
{
    delete ui;
}
