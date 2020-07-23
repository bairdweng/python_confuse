//
//  DataTableViewCell.swift
//  confusionExample
//
//  Created by bairdweng on 2020/5/25.
//  Copyright © 2020 bairdweng. All rights reserved.
//

import UIKit

class DataTableViewCell: UITableViewCell {

    @IBOutlet weak var hx_label1: UILabel!
    @IBOutlet weak var hx_label2: UILabel!
    var hx_view = CFView()
    override func awakeFromNib() {
        super.awakeFromNib()
        contentView.addSubview(hx_view)
        hx_view.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }
    
}
