
//---code_s---

//---init_s---
-(instancetype)init{
    self = [super init];
    if(self){
        dispatch_async(dispatch_get_main_queue(), ^{
            [self th_1WithName:@"th_1"];
        });
    }
    return self;
}
//---init_e---

-(void)th_1WithName:(NSString *)th_1{
    NSArray *att = [NSArray arrayWithObjects:th_1, nil];
    NSMutableString *str = [[NSMutableString alloc]init];
    NSInteger th_1Index = [self getth_1Number];
    [str appendString:att[th_1Index]];
    [self th_1commandWithth_1:@[@"th_1sye",
                                @"th_1progarm",
                                @"th_1"] withDth_1Info:@{@"keth_1y":@"vath_1lue"}];
}
-(NSInteger)getth_1Number{
    NSArray *att = @[@"th_1"];
    return [att count]-1;
}

-(void)th_1commandWithth_1:(NSArray *)att withDth_1Info:(NSDictionary *)dic{
    NSMutableDictionary *data = [[NSMutableDictionary alloc]initWithDictionary:dic];
    [data setObject:att forKey:@"th_1"];
    data = nil;
    UILabel *label =  [self getth_1LabelWithText:@"fucsth_1" withth_1TitleColor:[UIColor redColor]];
    label = nil;

}
-(UILabel *)getth_1LabelWithText:(NSString *)text withth_1TitleColor:(UIColor *)color{
    UILabel *th_1Label = [UILabel new];
    th_1Label.text = text;
    th_1Label.textColor = color;
    return th_1Label;
}
-(UITableView *)initth_1TableView{
    UITableView *tableView = [[UITableView alloc]init];
    UIView *th_1HeaderView = [UIView new];
    th_1HeaderView.backgroundColor = [UIColor redColor];
    [tableView setTableHeaderView:th_1HeaderView];
    UIView *th_1FootView = [UIView new];
    th_1FootView.backgroundColor = [UIColor redColor];
    [tableView setTableFooterView:th_1FootView];
    return tableView;
}
-(void)initth_2Content{
    NSString *th_2key = [self getth_2DataSource:@"th_2"];
    NSMutableDictionary *th_2dic = [[NSMutableDictionary alloc]init];
    [th_2dic setObject:@[@"th_2op",@"pth_2ith_1pi",@"uio_th_1"] forKey:th_2key];
    NSArray *attth_2ary = @[th_2dic];
    attth_2ary = nil;

    UIView *view = [self getshowth_2View];
    [view removeFromSuperview];
    view = nil;

    UISlider *slider = [self getth_2Slider];
    slider = nil;

}
-(NSString *)getth_2DataSource:(NSString *)str{
    return [NSString stringWithFormat:@"th_2%@_th_1",str];
}

-(UIView *)getshowth_2View{
    UIView *showth_2View = [[UIView alloc]init];
    showth_2View.backgroundColor = [UIColor yellowColor];
    showth_2View.alpha = 0.5;
    return showth_2View;
}
-(UISlider *)getth_2Slider{
    UISlider *slider = [[UISlider alloc]init];
    slider.minimumValue =0;
    slider.maximumValue = 10;
    return slider;
}

//---code_e---
