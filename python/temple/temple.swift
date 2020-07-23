

 //---code_s---

        func th_1codeInit() {
            th_1Name(th_1Text: "th_1")
        }
        
        func th_1Name(th_1Text:String) {
            let att = [th_1Text];
            th_1nicName(th_1Atts: att)
        }
        
        func th_1nicName(th_1Atts:[String]) {
            _ = th_1Atts
            th_1initTableView()
        }
        
        func th_1initTableView() {
            let th_1TableView = UITableView()
            th_1TableView.removeFromSuperview()
            th_2initBtn()
        }
        
        func th_2initBtn() {
            let th_1btn = UIButton()
            th_1btn.removeFromSuperview()
            th_1initLabel()
        }
        
        
        func th_1initLabel() {
            let th_1Label = UILabel()
            th_1Label.font = th_1initFont()
            th_1Label.removeFromSuperview()
            th_2initView()
        }
        func th_1initFont()->UIFont {
            let th_1Font = UIFont.systemFont(ofSize: 12)
            return th_1Font;
        }
        
        func th_2initView() {
            let th_2View = UICollectionView()
            th_2View.backgroundColor = th_2initColor()
            th_2View.removeFromSuperview()
            th_1InitCell()
        }
        func th_1InitCell() {
            let th_1Cell = UITableViewCell()
            th_1Cell.accessoryType = .detailButton
            th_1Cell.contentView.backgroundColor = th_2initColor()
            th_1Cell.removeFromSuperview()
            th_1layer()
        }
        
        func th_1layer() {
            let layer = CAShapeLayer()
            layer.fillColor = th_2initColor().cgColor
            layer.removeFromSuperlayer()
        }
        
        func th_2initColor()->UIColor {
            let th_2Color = UIColor()
            return th_2Color;
        }

//---code_e---


